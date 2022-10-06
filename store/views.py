import json
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from checkout.models import Order, OrderItem
from .models import Product


def store(request):
    products = Product.objects.all()
    # Set up pagination
    p = Paginator(Product.objects.all(), 6)
    page = request.GET.get('page')
    store_items = p.get_page(page)

    context = {
        'products': products,
        'store_items': store_items,
        }
    return render(request, 'store/store.html', context)


def item_update(request):
    data = json.loads(request.body)
    product_Id = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', product_Id)

    customer = request.user.customer
    product = Product.objects.get(id=product_Id)
    order, created = Order.objects.get_or_create(
        customer=customer,
        complete=False
        )

    orderItem, created = OrderItem.objects.get_or_create(
        order=order,
        product=product
        )

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
