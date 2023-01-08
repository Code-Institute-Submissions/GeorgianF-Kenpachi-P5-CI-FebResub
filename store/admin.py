from django.contrib import admin
from .models import Customer, Category, Product, Contact_us


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'contact_name',
        'contact_email',
        'contact_details',
        'sent_date',
        'email_status',
        )
    search_fields = ['contact_email', 'email_status']
    ordering = ('sent_date',)
    list_filter = ['email_status']


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
admin.site.register(Contact_us, ContactUsAdmin)
