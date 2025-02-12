from django.urls import path, include

from my_admin.views import *

from .shop_urls import shop_patterns
from .staff_urls import staff_patterns
from .orders_urls import orders_patterns
from .payments_urls import payments_patterns
from .services_overview_urls import services_overview_patterns

urlpatterns = [
    path("", view=DashBoardView.as_view(), name="admin/dashboard"),
    path("customers/", view=ListCustomerView.as_view(), name="admin/list-customer"),
    path("settings/",view=UpdateAdminView.as_view(), name="admin/settings"),
    path("services-overview/", include(services_overview_patterns)),
    path("shop/", include(shop_patterns)),
    path("staffs/",include(staff_patterns)),
    path("orders/",include(orders_patterns)),
    path("payments/",include(payments_patterns)),
]
