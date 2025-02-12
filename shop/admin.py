from django.contrib import admin
from .models import Category, Brand, Specification, Product, ProductSpec, ProductImage, ProductStock, Order, OrderItem, Payment

# Register your models here.


admin.site.register([Category, Brand, Specification, Product, ProductSpec, ProductImage, ProductStock, Order, OrderItem, Payment])