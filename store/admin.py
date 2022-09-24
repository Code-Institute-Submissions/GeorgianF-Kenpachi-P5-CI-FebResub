from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'email',
    )
    search_fields = ['name', 'email']

    ordering = ('user',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'price',
        'stock',
        'blade',
        'description',
    )
    list_filter = ('category', 'blade', 'stock')
    search_fields = ['name', 'blade', 'description']


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'date_ordered',
        'complete',
        'transaction_id',
    )
    list_filter = ('customer', 'date_ordered', )
    search_fields = ['customer', 'date_ordered', 'complete', 'transaction_id']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'order',
        'quantity',
        'date_added',
    )
    list_filter = ('product', 'order', 'date_added')
    search_fields = ['product', 'order', 'quantity', 'date_added']


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'order',
        'address',
        'city',
        'state',
        'country',
        'zipcode',
        'date_added',
    )
    list_filter = ('customer', 'order', 'city', 'date_added', 'country')
    search_fields = [
        'customer', 'order', 'address', 'country',
        'city', 'state', 'zipcode', 'date_added'
        ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
