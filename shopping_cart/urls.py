from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart/<str:pk>/', views.add_to_cart, name='add_to_cart'),
]
