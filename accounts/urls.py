from django.urls import path, include
from .views import index, register

urlpatterns = [
    path('', index),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]
