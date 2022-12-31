from django.shortcuts import render
from cart.utils import cart_details


def handler404(request, exception):
    """
    Error Handler 404 - Page Not Found
    """
    cart_info = cart_details(request)

    cart_items = cart_info['cart_items']
    order = cart_info['order']
    items = cart_info['items']

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
        }

    return render(request, 'home/404.html', context, status=404)
