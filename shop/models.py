from django.db import models
from accounts.models import CustomUser

from random import randrange

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):

    TYPES = [
        ("Pre-built PC", "Pre-built PC"),
        ("Refurbished Laptops & PC", "Refurbished Laptops & PC"),
        ("PC Components", "PC Components"),
        ("Monitors", "Monitors"),
        ("CCTV Cameras", "CCTV Cameras"),
        ("Software", "Software"),
        ("Peripherals", "Peripherals"),
    ]

    type = models.CharField(max_length=50, choices=TYPES)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    

class Specification(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="specs")
    key = models.CharField(max_length=100)

    def __str__(self):
        return self.key
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    warranty_periods = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    @property
    def image(self):
        url = self.images.filter(is_primary=True).first().image.url
        if url:
            return url
        return None
    
    @property

    def rating(self):
        rate = 3
        return {"rating": rate, "remain": 5 - rate}

    @property
    def available_stock(self):
        return self.stocks.filter(status="available").count()

    def __str__(self):
        return self.name
    

class ProductSpec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="specs")
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.name} - {self.specification.key}: {self.value}"
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='products/')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
                return f"Image of {self.product.name}"

    
class ProductStock(models.Model):

    STATUS = [
        ('available', 'Available'),
        ('freeze', 'Freeze'),
        ('sold', 'Sold'),
    ]


    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stocks")
    serial_number =  models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10, choices=STATUS, default='available')


    def __str__(self):
        return f"{self.product.name} - {self.serial_number} - {self.status}"


class Cart(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.user} | {self.product.name} | {self.quantity}"

class Order(models.Model):

    STATUS = [
            ('created', 'Created'), 
            ('confirmed', 'Confirmed'), 
            ('canceled', 'Canceled'),
            ('delivered', 'Delivered'),
        ]

    

    status = models.CharField(max_length=15, choices=STATUS, default='Created')
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="user_orders")
    date = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        total = 0

        for item in self.items.all():
            total += item.subtotal

        if total < 500:
            total += 40

        return total
    
    @property
    def item_description(self):
        return "TEST"

    def __str__(self):
        return f"Order from {self.user}"    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name="items")
    sku = models.ForeignKey(ProductStock, on_delete=models.DO_NOTHING)

    @property
    def subtotal(self):
        return 1 * self.product.price
    
    def __str__(self):
        return f"{self.product.name} | {self.product.price}"


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


    @property
    def total(self):
        return self.order.total
    

    payment_method = models.CharField(max_length=20, choices=METHOD)
    status = models.CharField(max_length=20, choices=STATUS)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payment")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} | {self.payment_method} | {self.status}"


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="ratings")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")