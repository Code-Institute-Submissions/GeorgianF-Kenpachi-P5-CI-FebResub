import json
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.db.models import Q
from checkout.models import Order, OrderItem, Customer, ShippingAddress
from cart.utils import cart_details
from .models import Contact_us
from .models import Product, Category
from .forms import ProductForm, GetInTouch
from cart.utils import cart_details


@never_cache
def store(request, category_slug=None):
    """
    A view to render the products into the store with pagination
    """
    categories = None
    products = None
    query = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories,
            is_available=True
            )
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    'You did not enter any information!')
                return redirect(reverse('store'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    cart_info = cart_details(request)

    cart_items = cart_info['cart_items']
    order = cart_info['order']
    items = cart_info['items']

    # Set up pagination
    paginator = Paginator(products.order_by('id'), 6)
    num_pages = paginator.page_range
    total_num_pages = paginator.num_pages
    page = request.GET.get('page')
    store_items = paginator.get_page(page)

    context = {
        'items': items,
        'products': store_items,
        'products_count': products_count,
        'cart_items': cart_items,
        'order': order,
        'num_pages': num_pages,
        'total_num_pages': total_num_pages,
        'search_term': query,
        }

    return render(request, 'store/store.html', context)


def contact(request):
    """
    A view to return the contact page
    """
    form = GetInTouch()
    if request.method == 'POST':
        form = GetInTouch(request.POST)
        if form.is_valid():
            form.save()
            form = GetInTouch()
            messages.success(
                request,
                'Message away!')
        else:
            messages.error(
                request,
                "There was an error with your request!"
                )
            form = GetInTouch()

    context = {'form': form}

    return render(request, 'store/contact.html', context)


@login_required
def view_message(request, message_id):
    """
    A view to display the messages to the admin
    """
    message = get_object_or_404(Contact_us, id=message_id)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    context = {
        'items': items,
        'cart_items': cart_items,
        'message': message
    }
    return render(request, 'store/view_message.html', context)


@login_required
def delete_message(request, message_id):
    """
    Delete a message from the admin profile
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('profile')

    message = get_object_or_404(Contact_us, id=message_id)
    message.delete()
    messages.success(request, 'Congrats, message deleted!')
    return redirect(reverse('profile'))


def product_details(request, product_id):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, pk=product_id)

    cart_info = cart_details(request)

    cart_items = cart_info['cart_items']
    order = cart_info['order']
    items = cart_info['items']

    context = {
        'product': product,
        'items': items,
        'cart_items': cart_items,
    }

    return render(request, 'store/product_details.html', context)


def product_details_add(request, product_id):
    """
    A view to add add to cart from the product details page
    """
    item_update(request)
    return redirect('cart')


def add_to_bag(request, product_id):
    """
    A view to add to cart for non-logged users
    """
    quantity = 1
    bag = request.session.get('cart', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag

    return redirect('cart')


def item_update(request):
    """
    A view to handle the actions and update items in the cart
    """
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(
        customer=customer,
        complete=False
        )
    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        product=product
        )

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
        messages.success(
                request,
                'Item has been added to cart')
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)
        messages.success(
                request,
                'Item has been removed from cart')

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)


@login_required
def profile(request):
    """
    A view to render the profile of the customer with order history
    """
    profile = get_object_or_404(Customer, user=request.user)
    orders = Order.objects.filter(customer=profile, complete=True)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    contact_messages = Contact_us.objects.all()

    context = {
        'items': items,
        'cart_items': cart_items,
        'orders': orders,
        'profile': profile,
        'contact_messages': contact_messages,
    }

    return render(request, 'store/profile.html', context)


@login_required
def view_order(request, transaction_id):
    """
    A view to render the order from the profile page
    """
    order = Order.objects.filter(transaction_id=transaction_id)[0]
    order_items = OrderItem.objects.filter(order=order)
    shipping_details = get_object_or_404(ShippingAddress, order=order)
    cart_info = cart_details(request)

    cart_items = cart_info['cart_items']
    items = cart_info['items']

    context = {
        'order': order,
        'order_items': order_items,
        'shipping_details': shipping_details,
        'cart_items': cart_items,
        'items': items,
    }

    return render(request, 'store/view_order.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store // admin only
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        add_form = ProductForm(request.POST, request.FILES)
        print(add_form)
        if add_form.is_valid():
            add_form.save()
            messages.success(
                request,
                'Successfully added the product to the store!'
                )
            return redirect('profile')
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
                )
    else:
        add_form = ProductForm()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    context = {
        'add_form': add_form,
        'items': items,
        'cart_items': cart_items,
    }

    return render(request, 'store/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store // admin only
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        edit_form = ProductForm(request.POST, request.FILES, instance=product)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('store'))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
                )
    else:
        edit_form = ProductForm(instance=product)
        messages.warning(request, f'You are editing {product.name}')

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    context = {
        'items': items,
        'cart_items': cart_items,
        'edit_form': edit_form,
        'product': product,
    }

    return render(request, 'store/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store // admin only
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('store')

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted from the store!')
    return redirect(reverse('store'))
