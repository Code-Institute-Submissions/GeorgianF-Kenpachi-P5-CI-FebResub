from django.db import models


class ContactForm(models.Model):
    """
    Contact form model
    """
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=50)
    contact_details = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.contact_name)
