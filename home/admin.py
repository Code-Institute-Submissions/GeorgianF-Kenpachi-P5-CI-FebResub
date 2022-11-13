from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        'contact_name',
        'contact_email',
        'contact_details',
        'created_at'
        )


contact_form = admin.site.register(ContactForm, ContactFormAdmin)
