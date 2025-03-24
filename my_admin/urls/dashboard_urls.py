from django.urls import path, include

from my_admin.views import *

from .shop_urls import shop_patterns
from .staff_urls import staff_patterns
from .orders_urls import orders_patterns
from .payments_urls import payments_patterns
from .services_overview_urls import services_overview_patterns
from .custom_url import custom_orders_patterns
from my_admin.views.warranty_views import *

urlpatterns = [
    path("", view=DashBoardView.as_view(), name="admin/dashboard"),
    path("customers/", view=ListCustomerView.as_view(), name="admin/list-customer"),

    # WARRANTY 

    path("warranty/", view=ListWarrantyView.as_view(), name="admin/list-warranty"),
    path("warranty/<int:pk>/", DetailWarrantyView.as_view(), name="warranty-detail"),


    # CLAIM
    path("claims/", view=ListWarrantyClaimView.as_view(), name="admin/list-claims"),
    path("claims/<int:pk>/", WarrantyClaimDetailView.as_view(), name="admin/claim-detail"),
    path("claims/update/<int:pk>/", WarrantyClaimUpdateView.as_view(), name="admin/claim-update"),



    path("settings/",view=UpdateAdminView.as_view(), name="admin/settings"),
    path("services-overview/", include(services_overview_patterns)),
    path("shop/", include(shop_patterns)),
    path("staffs/",include(staff_patterns)),
    path("orders/",include(orders_patterns)),
    path("custom/",include(custom_orders_patterns)),
    path("payments/",include(payments_patterns)),
]
