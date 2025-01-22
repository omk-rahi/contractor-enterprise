from django.db import models
from django.core.validators import MinValueValidator 

from accounts.models import CustomUser

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="services/")


    
class Quote(models.Model):
    description = models.TextField()
    suggested_price = models.IntegerField(validators=[MinValueValidator(1)], blank=True)

    STATUS = [
                ('pending', 'Pending'), 
                ('approved', 'Approved'), 
                ('rejected', 'Rejected')
            ]

    status = models.CharField(max_length=15, choices=STATUS)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name="service_qoutes")
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="user_service_quoutes")