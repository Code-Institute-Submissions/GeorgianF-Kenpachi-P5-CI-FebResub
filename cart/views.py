from django.shortcuts import render
from checkout.models import Order


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
    else:
        # Create empty cart for now for non-logged in user
        items = []

    context = {'items': items}
    return render(request, 'store/cart.html', context)
