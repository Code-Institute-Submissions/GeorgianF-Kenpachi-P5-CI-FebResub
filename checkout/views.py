from django.shortcuts import render


def checkout(request):
    context = {}
    return render(request, 'checkout/checkout.html', context)
