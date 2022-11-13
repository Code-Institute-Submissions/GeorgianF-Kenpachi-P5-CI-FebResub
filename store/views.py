import json
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages
from checkout.models import Order, OrderItem, Customer, ShippingAddress
from .models import Product, Category
from .forms import ProductForm


def store(request, category_slug=None):
    categories = None
    products = None

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

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        items = []
        print(items)
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = order['get_cart_items']

    # Set up pagination
    paginator = Paginator(products.order_by('id'), 6)
    page = request.GET.get('page')
    store_items = paginator.get_page(page)

    context = {
        'products': store_items,
        'products_count': products_count,
        'cart_items': cart_items,
        }

    return render(request, 'store/store.html', context)


def product_details(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        items = []
        print(items)
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = order['get_cart_items']

    context = {
        'product': product,
        'items': items,
        'cart_items': cart_items,
    }

    return render(request, 'store/product_details.html', context)


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_bag(request, product_id):
    quantity = 1
    bag = request.session.get('cart', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag

    return redirect('cart')


def item_update(request):
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
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    messages.success(
                request,
                'Item has been added to cart')

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)


@login_required
def profile(request):
    profile = get_object_or_404(Customer, user=request.user)
    orders = Order.objects.filter(customer=profile, complete=True)
    print(orders)
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
        'orders': orders,
        'profile': profile,
    }

    return render(request, 'store/profile.html', context)


@login_required
def view_order(request, transaction_id):
    order = Order.objects.filter(transaction_id=transaction_id)[0]
    print(order)
    order_items = OrderItem.objects.filter(order=order)
    shipping_details = get_object_or_404(ShippingAddress, order=order)
    print(shipping_details)

    context = {
        'order': order,
        'order_items': order_items,
        'shipping_details': shipping_details
    }

    return render(request, 'store/view_order.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        add_form = ProductForm(request.POST, request.FILES)
        print(add_form)
        if add_form.is_valid():
            product = add_form.save()
            messages.success(request, 'Successfully added the product to the store!')
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
