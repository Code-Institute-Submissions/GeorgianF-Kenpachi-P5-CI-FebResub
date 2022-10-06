import json
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages
from checkout.models import Order, OrderItem
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
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = order['get_cart_items']

    products = Product.objects.all()

    # Set up pagination
    p = Paginator(Product.objects.all(), 6)
    page = request.GET.get('page')
    store_items = p.get_page(page)

    context = {
        'products': products,
        'store_items': store_items,
        'cart_items': cart_items,
        }

    return render(request, 'store/store.html', context)


def item_update(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', product_id)

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
