from django.urls import path, include

from my_admin.views import *

from .services_urls import services_patterns
from .shop_urls import shop_patterns
from .staff_urls import staff_patterns
from .orders_urls import orders_patterns


urlpatterns = [
    path("", view=DashBoardView.as_view(), name="admin/dashboard"),
    path("services-overview/", view=ServicesOverview.as_view(), name="admin/services-overview"),
    path("customers/", view=ListCustomerView.as_view(), name="admin/list-customer"),
    path("settings/",view=UpdateAdminView.as_view(), name="admin/settings"),
    path("services/", include(services_patterns)),
    path("shop/", include(shop_patterns)),
    path("staffs/",include(staff_patterns)),
    path("orders/",include(orders_patterns)),
]
