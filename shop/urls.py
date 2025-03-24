from django.urls import path

from .views import *
from utils.payments import webhook_view

urlpatterns = [
    path('', index, name="home"), 

  


    path('shop/', ShopGrid.as_view(), name="shop"),
    path('shop/<int:pk>/', ProductDetail.as_view(), name="view-product"),
    path('shop/add-to-cart/', add_to_cart, name="add-to-cart"),
    path('shop/cart/', view_cart, name="view-cart"),
    path('shop/cart/plus/', cart_plus, name="cart-plus"),
    path('shop/cart/minus/', cart_minus, name="cart-minus"),
    path('shop/cart/checkout/', cart_checkout, name="cart-checkout"),
    path("shop/checkout/", checkout, name="checkout"),
    path("shop/order/success/", OrderSuccessView.as_view(), name="order-success"),
    path("orders/", view_orders, name="list-orders"),
    path("orders/<int:pk>/", OrderDetail.as_view(), name="order-detail"),
    path("orders/cancel/", cancel_order, name="cancel-order"),

    path("custom-orders/", view_custom_orders, name="list-custom-orders"),
    path("custom-orders/<int:pk>/", CustomOrderDetail.as_view(), name="custom-order-detail"),
    path("custom-orders/cancel/", cancel_custom_order, name="cancel-custom-order"),

    path("rating/", give_rating, name="give-rating"),

    path("submit-claim/", submit_warranty_claim, name="submit-claim"),
    path("warranty/success/", warranty_claim_success, name="warranty_claim_success"),
    path("warranty/expired/", warranty_claim_expired, name="warranty_claim_expired"),
    path("warranty/history/", warranty_claim_history, name="warranty_claim_history"),
    path("warranty/claim/<int:claim_id>/", warranty_claim_detail, name="warranty_claim_detail"),


    # BUILDER

    path("builder/", custom_pc_builder, name="builder"),
    path("builder-checkout/", builder_checkout, name="builder-checkout"),


    path("shop/payment/success/", PaymentSuccessView.as_view()),
    path("shop/payment/cancel/", PaymentCancelView.as_view()),
    path("stripe/webhook/", webhook_view),

]
