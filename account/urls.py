from django.urls import path
from . import views

urlpatterns = [
    path('account/logout/', views.logout_view, name='logout'),
]
