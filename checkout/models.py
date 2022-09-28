from django.db import models
from django_countries.fields import CountryField
from store.models import Customer, Product


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.transaction_id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    class Meta:
        verbose_name_plural = 'Shipping Address'

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True
        )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True
        )
    address = models.CharField(max_length=200, null=False, blank=False)
    city = models.CharField(max_length=200, null=False, blank=False)
    state = models.CharField(max_length=200, blank=True, null=False)
    zipcode = models.CharField(max_length=200, null=False, blank=False)
    country = CountryField(null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)
