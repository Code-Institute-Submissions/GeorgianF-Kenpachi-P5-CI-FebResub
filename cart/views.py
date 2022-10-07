import json
from django.http import JsonResponse
from django.shortcuts import render
from checkout.models import Order, OrderItem
from store.models import Product


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False,
            )
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
            print('CART:', cart)

        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
            }
        cart_items = order['get_cart_items']

        for i in cart:
            cart_items += cart[i]['quantity']

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
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was changed', safe=False)
