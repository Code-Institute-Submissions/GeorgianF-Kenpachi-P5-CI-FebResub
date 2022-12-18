from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem


class ShippingAddressAdminInline(admin.TabularInline):
    model = ShippingAddress


class OrderAdmin(admin.ModelAdmin):
    inlines = (
        OrderItemAdminInline,
        ShippingAddressAdminInline,
        )

    list_display = (
        'customer',
        'date_ordered',
        'complete',
        'transaction_id',
        'get_cart_total',
        'get_cart_items'
    )
    list_filter = ('customer', 'date_ordered', 'complete')
    search_fields = ['customer', 'date_ordered', 'complete', 'transaction_id']


admin.site.register(Order, OrderAdmin)
