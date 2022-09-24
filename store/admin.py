from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'email',
    )

    ordering = ('user',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'price',
        'description',
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'date_ordered',
        'complete',
        'transaction_id',
    )


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'order',
        'quantity',
        'date_added',
    )


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'order',
        'address',
        'city',
        'state',
        'zipcode',
        'date_added',
    )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
