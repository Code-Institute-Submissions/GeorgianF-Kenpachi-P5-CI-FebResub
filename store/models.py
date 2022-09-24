from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    STEEL = (
        ('Maru Steel', (
            ('T10 steel', 'T10 steel'),
            ('1095 steel', '1095 steel'),
            ('Manganese steel', 'Manganese steel'),
        )),
        ('Damascus Steel', 'Damascus Steel'),
        ('Kobuse Forge Steel', 'Kobuse Forge Steel'),
        ('San-Mai Forge Steel', 'San-Mai Forge Steel'),
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=200)
    price = models.FloatField()
    blade = models.CharField(choices=STEEL, max_length=200, null=True)
    guard = models.CharField(max_length=200, null=True)
    scabbard = models.CharField(max_length=200, null=True)
    handle = models.CharField(max_length=200, null=True)
    length_with_sleeve = models.FloatField(null=True)
    length_of_the_blade = models.FloatField(null=True)
    length_of_the_handle = models.FloatField(null=True)
    width_of_the_blade = models.FloatField(null=True)
    blade_thickness = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


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
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, blank=True, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)
