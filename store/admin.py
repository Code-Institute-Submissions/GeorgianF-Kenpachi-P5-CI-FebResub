from django.contrib import admin
from .models import Customer, Category, Product


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'last_name',
        'email',
    )
    search_fields = ['name', 'email']

    ordering = ('user',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

    list_display = (
        'name',
        'slug',
        'description',
    )


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

    list_display = (
        'category',
        'slug',
        'name',
        'price',
        'stock',
        'blade',
        'is_available',
    )
    list_filter = ('category', 'blade', 'stock')
    search_fields = ['name', 'blade', 'description']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
