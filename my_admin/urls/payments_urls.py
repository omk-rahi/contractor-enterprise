from django.urls import path

from my_admin.views.payments_view import *

payments_patterns = [
    path("", view=ListPaymentView.as_view(), name="admin/list-payment"),
]
