from django.contrib import admin

from .models import UserStripe, UserAddres

# Register your models here.

admin.site.register(UserStripe)
admin.site.register(UserAddres)