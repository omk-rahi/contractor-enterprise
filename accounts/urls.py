from django.urls import path, include
from .views import index, register, verify, send_otp

urlpatterns = [
    path('', index),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('verify/', verify, name='verify'),
    path('verify/send', send_otp, name='verify-send-otp'),
]
