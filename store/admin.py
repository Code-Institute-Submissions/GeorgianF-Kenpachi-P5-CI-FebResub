from django.contrib import admin
from .models import Customer, Category, Product


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
    )
    list_filter = ('category', 'blade', 'stock')
    search_fields = ['name', 'blade', 'description']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
