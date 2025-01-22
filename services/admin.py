from django.contrib import admin

from .models import Service, Quote

# Register your models here.

admin.site.register([Service, Quote])