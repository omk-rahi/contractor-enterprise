from django.db import models

from accounts.models import CustomUser

from cloudinary.models import CloudinaryField

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = CloudinaryField("image")

    def __str__(self):
        return self.name
    

class ServiceCost(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="costs")
    description = models.CharField(max_length=100)
    estimated_cost = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description}"


class Quote(models.Model):
    description = models.TextField()

    STATUS = [
                ('pending', 'Pending'), 
                ('approved', 'Approved'), 
                ('rejected', 'Rejected')
            ]
    
    
    @property
    def user_phone(self):
        return self.user.phone
    @property
    def user_address(self):
        try :
            return self.user.address
        except:
            return "No address found"
        
    
    
    status = models.CharField(max_length=15, choices=STATUS, default="pending")
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name="quotes")
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="quotes")
    estimated_cost = models.PositiveIntegerField(null=True, default=0)
    problem = models.OneToOneField(ServiceCost, on_delete=models.CASCADE, related_name="problem", null=True, default=None)


    def __str__(self):
        return f"Quote on {self.service.name} by {self.user.fullname}"


class Booking(models.Model):

    STATUS = [
        ('created', 'Created'), 
        ('scheduled', 'Scheduled'), 
        ('in_process', 'In Process'), 
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name="bookings")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="bookings")
    staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="assigned_bookings", null=True)

    additional_note = models.TextField()

    cost = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default='Created')
    scheduled_date = models.DateField(null=True)
    booking_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"Booking of {self.service.name} by {self.user.fullname}"
