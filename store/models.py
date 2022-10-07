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
    email = models.EmailField(max_length=254)

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
    price = models.DecimalField(max_digits=10, decimal_places=2)
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
    stock = models.IntegerField(blank=False, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
