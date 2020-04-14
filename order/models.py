from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from account.models import UserAddres
from shopping_cart.models import Cart

# Create your models here.

STATUS_CHOICES = (
    ('Started', 'Started'),
    ('Abandoned', 'Abandoned'),
    ('Finished', 'Finished'),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.CharField(max_length=120, unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')
    
    address = models.ForeignKey(UserAddres, on_delete=models.SET_NULL, blank=True, null=True)
    
    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id


    def get_final_tax_amount(self):
        instance = Order.objects.get(id=self.id)
        two_decimals = Decimal(10) ** -2
        instance.tax_total = Decimal(Decimal('0.24') * Decimal(self.sub_total)).quantize(two_decimals)
        instance.save()

        return  instance.tax_total

    def get_final_amount(self):
        instance = Order.objects.get(id=self.id)
        instance.final_total = Decimal(self.sub_total) + Decimal(instance.tax_total)
        instance.save()

        return  instance.final_total