from django.db import models
from datetime import datetime

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class VariatonManager(models.Manager):
    def all(self):
        return super(VariatonManager, self).filter(active=True)

    def sizes(self):
        return self.all().filter(category='size')

    def colors(self):
        return self.all().filter(category='color')


VAR_CATEGORIES = (
    ('size', 'size'),
    ('color', 'color'),
    )


class Variaton(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    objects = VariatonManager()

    def __str__(self):
        return self.title