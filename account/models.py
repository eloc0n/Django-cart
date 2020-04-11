from django.conf import settings
from django.db import models

# Create your models here.

class UserAddres(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=120)
    shipping = models.BooleanField(default=True)
    billing = models.BooleanField(default=False)
    message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    

    def __str__(self):
        return str(self.user.username)



class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    stripe_id = models.CharField(max_length=120)

    def __str__(self):
        return self.stripe_id

