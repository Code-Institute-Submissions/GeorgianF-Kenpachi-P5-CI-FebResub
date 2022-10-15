import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages
from checkout.models import Order, OrderItem, Customer
from .models import Product


def store(request):
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

    products = Product.objects.all().filter(is_available=True)

    # Set up pagination
    p = Paginator(Product.objects.all().filter(is_available=True), 6)
    page = request.GET.get('page')
    store_items = p.get_page(page)

    context = {
        'products': products,
        'store_items': store_items,
        'cart_items': cart_items,
        }

    return render(request, 'store/store.html', context)


def product_details(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'store/product_details.html', context)


def add_to_bag(request, product_id):
    quantity = 1
    bag = request.session.get('cart', {})
    print(bag)
    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag

    print(request.session['bag'])
    print(bag.keys())
    print(bag.items())

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
    print(profile)
    orders = Order.objects.filter(customer=profile, complete=True)
    print(orders)

    context = {
        'orders': orders,
        'profile': profile
    }

    return render(request, 'store/profile.html', context)
