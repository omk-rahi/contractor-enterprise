from django.urls import path

from my_admin.views.orders_views import *

orders_patterns = [
    path("", view=ListOrderView.as_view(), name="admin/list-order"),
    path("<int:pk>", view=OrderDetailView.as_view(), name="admin/view-order"),
    path("update/<int:pk>/", view=UpdateOrderView.as_view(), name="admin/update-order"),
]
