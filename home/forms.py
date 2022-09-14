from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField
from .models import ContactForm


class GetInTouch(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(FloatingField(
            "contact_name",
            "contact_email",
            "contact_details")
            )
        self.helper.form_method = 'POST'
        self.helper.add_input(
            Submit('submit', 'Submit'),
            )

    contact_name = forms.CharField(
        label="Your full name here...",
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
            ))
    contact_email = forms.EmailField(label="Your email here...")
    contact_details = forms.CharField(widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                }
            ))

    class Meta:
        model = ContactForm
        fields = "__all__"
