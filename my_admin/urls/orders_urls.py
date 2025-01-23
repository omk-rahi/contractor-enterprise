from django.urls import path

from my_admin.views.orders_views import *

orders_patterns = [
    path("", view=ListOrderView.as_view(), name="admin/list-order"),
]
