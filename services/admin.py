from django.contrib import admin

from .models import Service, ServiceCost, Quote, Booking, Feedback

# Register your models here.

admin.site.register([Service, ServiceCost, Quote, Booking, Feedback])