from django.forms import ModelForm
from django import forms
from .models import ContactForm


class GetInTouch(ModelForm):
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
        model = ContactForm
        fields = "__all__"
