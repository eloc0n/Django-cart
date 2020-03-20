from django.db import models
from datetime import datetime

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title