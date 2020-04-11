from django.contrib.auth.models import User
from django.db import models

from shopping_cart.models import Cart

# Create your models here.

STATUS_CHOICES = (
    ('Started', 'Started'),
    ('Abandoned', 'Abandoned'),
    ('Finished', 'Finished'),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')
    
    # address **
    
    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id

    def get_final_amount(self):
        instance = Order.objects.get(id=self.id)
        instance.tax_total = 0.24 * float(self.sub_total)
        instance.final_total = float(self.sub_total) + float(instance.tax_total)
        instance.save()

        return  round(instance.final_total, 2)