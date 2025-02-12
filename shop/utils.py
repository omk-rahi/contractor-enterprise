from .models import  ProductStock

def get_stock(product):
    
    stock = ProductStock.objects.filter(product=product, status="available").first()

    if stock:
        return stock
    
    return None


def freeze_stock(stock):
    stock.status = "freeze"
    stock.save()

def get_checkout_total_cart(items):
    subtotal = 0
    delivery_charge = 0


    for item in items:
        subtotal += item.total

    if subtotal < 500:
        delivery_charge = 40

    total = subtotal + delivery_charge

    return subtotal, delivery_charge, total

def get_checkout_total_product(products):

    subtotal = 0
    delivery_charge = 0

    for product in products:
        subtotal += product.price
    
    if subtotal < 500:
        delivery_charge = 40

    total = subtotal + delivery_charge

    return subtotal, delivery_charge, total