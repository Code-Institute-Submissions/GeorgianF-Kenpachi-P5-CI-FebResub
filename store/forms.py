from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
