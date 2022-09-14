from django.shortcuts import render


def cart(request):
    context = {}
    return render(request, 'cart/cart.html', context)
