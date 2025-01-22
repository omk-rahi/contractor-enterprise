from django.db import models
from django.contrib.auth.models import AbstractUser

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
    profile_image = models.ImageField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.fullname}"
