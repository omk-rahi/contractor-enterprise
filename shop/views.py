from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from accounts.models import Address
from accounts.forms import AddressForm
from .forms import CheckoutForm, WarrantyClaimForm
from django.db.models import Q, Avg, Count

from .utils import get_stock, freeze_stock, get_checkout_total_cart, get_checkout_total_product

from utils.payments import create_checkout_session

from django.utils.timezone import now


# Create your views here.

def index(request):

    if request.user.is_superuser:
        return redirect("/admin")
    
    products = list(Product.objects.annotate(
        avg_rating=Avg('reviews__rating'),
        review_count=Count('reviews')
    ).order_by('-avg_rating')[:3])


    return render(request, 'shop/homepage.html', context={"products": products})

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
                Payment.objects.create(order=order, payment_method="COD", stripe_id="", status="pending")

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

                Payment.objects.create(order=order, payment_method="COD", status="pending")


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

    items = order.items.all()

    for item in items:
        item.sku.status = "available"
        item.sku.save()


    order.status = 'canceled'
    order.save()

    return redirect(request.META.get("HTTP_REFERER", "home"))


# RATINGS

@login_required
def give_rating(request):
    if request.method != "POST":
        return redirect('home')

    rating = request.POST["rating"]
    feedback = request.POST["feedback"]
    product_id = request.POST["product"]
    product = get_object_or_404(Product, pk=product_id)

    if not rating or not feedback or not product_id:
        messages.error(request, "Please provide all required fields.")
        return redirect(request.META.get('HTTP_REFERER', '/'))

    existing_review = Reviews.objects.filter(user=request.user, product=product).first()
    if existing_review:
        messages.error(request, "You have already reviewed this product.")
        return redirect(request.META.get('HTTP_REFERER', '/'))

    Reviews.objects.create(product=product, user=request.user, rating=rating, feedback=feedback)
    messages.success(request, "Review published successfully!")
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


# CLAIM

@login_required
def submit_warranty_claim(request):
    orders = Order.objects.filter(user=request.user, status="delivered")  
    order_items = OrderItem.objects.filter(order__user=request.user, warranty__warranty_end_date__gte=now().date())

    if request.method == "POST":
        form = WarrantyClaimForm(request.POST)
        if form.is_valid():
            order_item = form.cleaned_data["order_item"]
            warranty = Warranty.objects.filter(order_item=order_item).first()

            if not warranty or not warranty.is_valid():
                return redirect("warranty_claim_expired")

            claim = form.save(commit=False)
            claim.user = request.user
            claim.save()
            return redirect("warranty_claim_success")

    else:
        form = WarrantyClaimForm()
        form.fields["order_item"].queryset = order_items

    return render(request, "shop/submit-claim.html", {"form": form, "orders": orders})


def warranty_claim_success(request):
    return render(request, "shop/claim_success.html")

def warranty_claim_expired(request):
    return render(request, "shop/claim_expired.html")

@login_required
def warranty_claim_history(request):
    claims = WarrantyClaim.objects.filter(user=request.user)
    return render(request, "shop/warranty_claim_history.html", {"claims": claims})

@login_required
def warranty_claim_detail(request, claim_id):
    claim = get_object_or_404(WarrantyClaim, id=claim_id, user=request.user)
    return render(request, "shop/warranty_claim_detail.html", {"claim": claim})



# BUILDER

def custom_pc_builder(request):
    components = ["Motherboards", "Processors", "Graphics Cards", "Memory", "Storage Drives", "Power Supply Units", "PC Cabinet", "CPU Cooler", "Case Fans", "Keyboard", "Mouse"]
    categories = Category.objects.filter(name__in=components)
    components = [
        {
            "name": category.name,
            "products": Product.objects.filter(category=category)
        }
        for category in categories
    ]
    return render(request, "shop/builder.html", {"components": components})


@login_required
def builder_checkout(request):
    address = get_object_or_404(Address, user=request.user)

    if request.method == "POST":
        selected_components = request.GET.getlist("selected_components")

        products = Product.objects.filter(id__in=selected_components)
        subtotal = sum(product.price for product in products)
        build_charge = 0  
        total = subtotal  

        address_form = AddressForm(request.POST, instance=address)
        checkout_form = CheckoutForm(request.POST, instance=request.user)

        if address_form.is_valid() and checkout_form.is_valid():
            address_form.save()
            checkout_form.save()

            custom_build = CustomPCBuild.objects.create(
                user=request.user,
                name=f"Custom PC - {request.user.username}",
                total_price=total
            )

            for product in products:
                PCBuildItem.objects.create(
                    build=custom_build,
                    product=product,
                    component_type=product.category 
                )

            messages.success(request, "Custom PC Build order placed successfully!")
            return redirect("order-success")

    else:
        selected_components = request.GET.getlist("selected_components")

        if len(selected_components) < 11:
            messages.error(request, "Please select all components")
            return redirect("builder")
        else:
            products = Product.objects.filter(id__in=selected_components)
            subtotal = sum(product.price for product in products)
            build_charge = 0  # Adjust if necessary
            total = subtotal  

            address_form = AddressForm(instance=address)
            checkout_form = CheckoutForm(instance=request.user)

            context = {
                "address_form": address_form,
                "checkout_form": checkout_form,
                "products": products,
                "subtotal": subtotal,
                "build_charge": build_charge,
                "total": total,
            }
            return render(request, "shop/builder_checkout.html", context)


@login_required
def view_custom_orders(request):
    custom_orders = CustomPCBuild.objects.filter(user=request.user)

    context = {
        "custom_orders": custom_orders
    }

    return render(request, "shop/custom_orders.html", context)


class CustomOrderDetail(LoginRequiredMixin, DetailView):
    model = CustomPCBuild
    template_name = "shop/custom_order_detail.html"


@login_required
def cancel_custom_order(request):
    if request.method != "POST":
        return redirect('home')

    order_id = request.POST.get("order_id")
    custom_order = get_object_or_404(CustomPCBuild, pk=order_id, user=request.user)

    for item in custom_order.items.all():
        item.product.status = "available"
        item.product.save()

    custom_order.delete()
    messages.success(request, "Your custom PC build order has been canceled.")
    return redirect(request.META.get("HTTP_REFERER", "custom_orders"))
