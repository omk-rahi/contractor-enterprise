from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, Order, OrderItem, Brand, Category
from django.contrib import messages
from accounts.models import Address
from accounts.forms import AddressForm
from .forms import CheckoutForm
from django.db.models import Q

from .utils import get_stock, freeze_stock, get_checkout_total_cart, get_checkout_total_product

from utils.payments import create_checkout_session

# Create your views here.

def index(request):

    if request.user.is_superuser:
        return redirect("/admin")

    return render(request, 'shop/homepage.html')

class ShopGrid(ListView):
    model = Product
    template_name = 'shop/shop-grid.html'
    paginate_by = 12
    order_by = ["name"]

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get("query", None)
        category = self.request.GET.get("category", None)
        brands = self.request.GET.getlist("brand", None)
        type = self.request.GET.get("type", None)
        sort = self.request.GET.get("sort", None)

        
        if query:
           queryset = queryset.filter(
                                        Q(name__icontains=query) | 
                                        Q(description__icontains=query) | 
                                        Q(category__name__icontains=query) |
                                        Q(brand__name__icontains=query)
                                    )
           
        if category:
            queryset = queryset.filter(category__name__icontains=category)

        if type:
            queryset = queryset.filter(category__type__icontains=type)

        if brands:
            queryset = queryset.filter(brand__name__in=brands)


        if sort:
            queryset = queryset.order_by(sort)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context["categories"] = Category.objects.filter(products__in=queryset).distinct()
            
        context["brands"] = Brand.objects.filter(products__in=queryset).distinct()

        return context
    



class ProductDetail(DetailView):
    model = Product
    template_name = "shop/product-detail.html"


@login_required
def view_cart(request):

    items = Cart.objects.filter(user=request.user)

    subtotal, delivery_charge, total = get_checkout_total_cart(items=items)

    context = {
        "items": items, 
        "subtotal": subtotal, 
        "delivery_charge": delivery_charge, 
        "total": total
    }

    return render(request, 'shop/cart.html', context=context)



@login_required
def add_to_cart(request):

    if request.POST:

        pk = request.POST["product_id"]

        product = get_object_or_404(Product, pk=pk)
        
        try:
            # CHECK IF THE PRODUCT EXIT IN CART
            item = get_object_or_404(Cart, user=request.user, product=product)
            
            stock = get_stock(item.product)

            if not stock:
                messages.error(request, "We don't have more item in stock")
                return redirect(reverse_lazy("view-product", kwargs={"pk": pk}))

            if item.quantity < 5:
                item.quantity += 1
                item.save()
                messages.success(request, "Item added to cart.")
                
            else:
                messages.error(request, "You can't add more than 5 of this item.")
        except:
            # Add to cart
            quantity = request.POST['quantity']
            Cart.objects.create(user=request.user, product=product, quantity=quantity)
            messages.success(request, "Item added to cart.")

        
        return redirect(reverse_lazy("view-product", kwargs={"pk": pk}))
    
    return redirect("home")


@login_required
def cart_plus(request):
    if not request.POST:
        return redirect("home")
    
    item_id = request.POST["item_id"]

    item = get_object_or_404(Cart, pk=item_id)

    stock = get_stock(item.product)

    if not stock:
        messages.error(request, "We don't have more item in stock")
        return redirect('view-cart')


    if item.quantity < 5:
        item.quantity += 1
        item.save()

    return redirect('view-cart')

@login_required
def cart_minus(request):
    if not request.POST:
        return redirect("home")
    
    item_id = request.POST["item_id"]

    item = get_object_or_404(Cart, pk=item_id)

    if item.quantity == 1:
        item.delete()
    else:
        item.quantity -= 1
        item.save()

    return redirect('view-cart')


# Payment 
@login_required
def checkout(request):

    address = get_object_or_404(Address, user=request.user)
    product_id = request.GET.get("product_id")
    product = get_object_or_404(Product, pk=product_id)
    payment_mode = request.POST.get("payment_mode")

    if request.POST:
        address_form = AddressForm(request.POST, instance=address)
        checkout_form = CheckoutForm(request.POST, instance=request.user)

        stock = get_stock(product=product)

        if stock is None:
            messages.error(request, "Product is out of stock")
            return redirect("home")

        if address_form.is_valid() and checkout_form.is_valid():
            address_form.save()
            checkout_form.save()

            # CHECK PAYMENT MODE
            if payment_mode == 'cod':
                order = Order.objects.create(user=request.user)
                OrderItem.objects.create(order=order, product=product, sku=stock)

                freeze_stock(stock=stock)

                return redirect("order-success")

            else:
                session = create_checkout_session(request.user, items=[product])
                return redirect(session.url)

    else:
        address_form = AddressForm(instance=address)
        checkout_form = CheckoutForm(instance=request.user)
        subtotal, delivery_charge, total = get_checkout_total_product([product])

        context = {
            "address_form": address_form, 
            "checkout_form": checkout_form, 
            "subtotal": subtotal, 
            "delivery_charge": delivery_charge,
            "total": total,
            "product": product
        }

        return render(request, "shop/checkout.html", context=context)


@login_required
def cart_checkout(request):
    address = get_object_or_404(Address, user=request.user)
    items = Cart.objects.filter(user=request.user)
    payment_mode = request.POST.get("payment_mode")
    address_form = AddressForm(instance=address)
    checkout_form = CheckoutForm(instance=request.user)
    subtotal, delivery_charge, total = get_checkout_total_cart(items=items)

    products = []

    for item in items:
        if item.quantity > 1:
            products.extend([item.product] * item.quantity)
        else:
            products.append(item.product)

    if request.POST:
        address_form = AddressForm(request.POST, instance=address)
        checkout_form = CheckoutForm(request.POST, instance=request.user)

        if address_form.is_valid() and checkout_form.is_valid():
            address_form.save()
            checkout_form.save()

            # CHECK PAYMENT MODE
            if payment_mode == 'cod':
                order = Order.objects.create(user=request.user)

                for product in products:
                    stock = get_stock(product=product)
                    OrderItem.objects.create(order=order, product=product, sku=stock)
                    freeze_stock(stock=stock)

                for item in items:
                    item.delete()

                return redirect("order-success")

            else:
                session = create_checkout_session(request.user, items=products)
                return redirect(session.url)
    

    context = {
        "address_form": address_form, 
        "checkout_form": checkout_form, 
        "subtotal": subtotal, 
        "delivery_charge": delivery_charge,
        "total": total,
        "cart_items": items
    }

    return render(request, "shop/checkout.html", context=context)

class OrderSuccessView(TemplateView):
    template_name = "shop/order-success.html"

class PaymentSuccessView(TemplateView):
    template_name = "shop/payment-success.html"

class PaymentCancelView(TemplateView):
    template_name = "shop/payment-cancel.html"


# ORDERS

@login_required
def view_orders(request):

    orders = Order.objects.filter(user=request.user)

    context = {
        "orders": orders
    }

    return render(request, "shop/orders.html", context)


class OrderDetail(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "shop/order-detail.html"

@login_required
def cancel_order(request):
    if request.method != "POST":
        return redirect('home')

    order_id = request.POST.get("order_id")

    order = get_object_or_404(Order, pk=order_id)

    order.status = 'canceled'
    order.save()

    return redirect(request.META.get("HTTP_REFERER", "home"))
