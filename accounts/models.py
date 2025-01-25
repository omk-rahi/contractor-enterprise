from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets
from django.utils.timezone import now

from .manager import CustomUserManager

# Create your models here.

USER_ROLES = (
    ('customer', 'Customer'),
    ('admin', 'Admin'),
    ('staff', 'Staff'),
)

class CustomUser(AbstractUser):
    username = None
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=15, choices=USER_ROLES, default='customer')
    profile_image = models.ImageField(blank=True, upload_to='users/')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.fullname}"

class OTP(models.Model):
    code = models.CharField(max_length=6)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_valid(self):
        return now() < self.expires_at