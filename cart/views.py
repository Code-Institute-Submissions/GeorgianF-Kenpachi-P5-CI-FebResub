import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from checkout.models import Order, OrderItem
from store.models import Product
from .utils import cart_details


def cart(request):
    cart_info = cart_details(request)

    cart_items = cart_info['cart_items']
    order = cart_info['order']
    items = cart_info['items']

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
        }

    return render(request, 'cart/cart.html', context)


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
        messages.success(
            request,
            "Item has been added to the cart!"
        )
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)
        messages.success(
            request,
            "Item has been removed from the cart!"
        )

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was changed', safe=False)
