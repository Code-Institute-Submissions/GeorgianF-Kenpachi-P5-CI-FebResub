from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.forms.widgets import ClearableFileInput
from .models import Product, Contact_us


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(FloatingField(
            'category',
            'name',
            'price',
            'blade',
            'guard',
            'scabbard',
            'handle',
            'length_with_sleeve',
            'length_of_the_blade',
            'length_of_the_handle',
            'width_of_the_blade',
            'blade_thickness',
            'weight',
            'description',
            'stock',
            'is_available',
            'image',
            ))

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=ClearableFileInput
        )

    class Meta:
        model = Product
        fields = (
            'category',
            'name',
            'price',
            'blade',
            'guard',
            'scabbard',
            'handle',
            'length_with_sleeve',
            'length_of_the_blade',
            'length_of_the_handle',
            'width_of_the_blade',
            'blade_thickness',
            'weight',
            'description',
            'stock',
            'image',
        )


class GetInTouch(forms.ModelForm):
    contact_name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
            ))
    contact_email = forms.EmailField(label="Email Address")
    contact_details = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5',
                }
            ))

    class Meta:
        model = Contact_us
        fields = (
            'contact_name',
            'contact_email',
            'contact_details',
        )
