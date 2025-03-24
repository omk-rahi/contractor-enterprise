from django.urls import path

from my_admin.views.custom_views import *

custom_orders_patterns = [
    path("", view=ListCustomOrderView.as_view(), name="admin/list-custom-order"),
    path("<int:pk>", view=CustomOrderDetailView.as_view(), name="admin/view-custom-order"),
    path("update/<int:pk>", view=UpdateCustomOrderView.as_view(), name="admin/update-custom-order"),
]