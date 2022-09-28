from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress


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


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
