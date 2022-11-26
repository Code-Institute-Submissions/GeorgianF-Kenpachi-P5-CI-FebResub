import json
import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Order, ShippingAddress


def checkout(request):
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
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0
            }
        cart_items = order['get_cart_items']

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
        }
    return render(request, 'checkout/checkout.html', context)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            country=data['shipping']['country'],
        )

    else:
        print('User is not logged in')

    return JsonResponse('Transaction complete!', safe=False)
