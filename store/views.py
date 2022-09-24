from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


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
