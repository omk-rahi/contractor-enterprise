from django.urls import path, include
from .views import index, register, verify, send_otp, user_settings, save_address, save_profile
from django.contrib.auth.views import PasswordChangeView, PasswordResetConfirmView
from .forms import CustomPasswordChangeForm, CustomSetPasswordForm

urlpatterns = [
    path('', index),
    path('register/', register, name='register'),
    path('verify/', verify, name='verify'),
    path('verify/send', send_otp, name='verify-send-otp'),
    path('password_change/', PasswordChangeView.as_view(form_class=CustomPasswordChangeForm), name='password-change'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(form_class=CustomSetPasswordForm), name='password-reset-confirm'),
    path('settings/', user_settings, name='user-settings'),
    path('settings/save-address', save_address, name='save-address'),
    path('settings/save-profile', save_profile, name='save-profile'),
    path('', include('django.contrib.auth.urls')),
]
