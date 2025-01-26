from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import CustomUser

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    warranty_periods = models.IntegerField(validators=[MinValueValidator(1)])
    base_price = models.PositiveBigIntegerField()
    available_stock = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")


    def __str__(self):
        return self.name
    

class Specification(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="specs")

    def __str__(self):
        return f"{self.key} - {self.value}"


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    is_primary = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"Image of {self.product.name}"
    

class ProductOption(models.Model):

    OPTIONS = [
        ("Size", "Size"),
        ("Color", "Color"),
        ("Capacity", "Capacity"),
        ("Speed", "Speed"),
        ("Type", "Type"),

    ]

    option = models.CharField(max_length=20, choices=OPTIONS)
    value = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="options")

    

class Order(models.Model):

    STATUS = [
            ('created', 'Created'), 
            ('confirmed', 'Confirmed'), 
            ('in_process', 'In Process'),
            ('canceled', 'Canceled'),
            ('delivered', 'Delivered'),
        ]

    

    status = models.CharField(max_length=15, choices=STATUS, default='Created')
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="user_orders")
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Order from {self.user}"
    
    def get_total_str(self):
        return '₹800 (5 Products)'
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="product")
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name="orders")
    quantity = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()

    
    def __str__(self):
        return f"{self.product.name} | {self.quantity} | ₹{self.price}"


class Payment(models.Model):

    STATUS = [
        ('pending', 'Pending'), 
        ('completed', 'Completed'), 
        ('failed', 'Failed'),
        ('rejected', 'Rejected'),
    ]

    METHOD = [
        ("COD", "COD"), 
        ("Online", "Online")
        ]


    amount = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=20, choices=METHOD)
    status = models.CharField(max_length=20, choices=STATUS)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payment")
    date = models.DateTimeField(auto_now_add=True)

    def get_total_str(self):
        return '₹800'