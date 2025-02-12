from django.urls import path

from my_admin.views.services_views import *
from my_admin.views.service_cost_views import *

services_patterns = [
    path("", ListServiceView.as_view(), name="admin/list-service"),
    path("<int:pk>/", view=ListServiceCostView.as_view(), name="admin/list-service-cost"),
    path("<int:service_pk>/create/", view=CreateServiceCostView.as_view(), name="admin/create-service-cost"),
    path("<int:service_pk>/update/<int:pk>/", view=UpdateServiceCostView.as_view(), name="admin/update-service-cost"),
    path("<int:service_pk>/delete/<int:pk>/", view=DeleteServiceCostView.as_view(), name="admin/delete-service-cost"),
    path("create/", view=CreateServiceView.as_view(), name="admin/create-service"),
    path("update/<int:pk>/", view=UpdateServiceView.as_view(), name="admin/update-service"),
    path("delete/<int:pk>/", view=DeleteServiceView.as_view(), name="admin/delete-service"),
    
]