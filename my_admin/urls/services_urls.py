from django.urls import path

from my_admin.views.services_views import *

services_patterns = [
    path("", ListServiceView.as_view(), name="admin/list-service"),
    path("create/", view=CreateServiceView.as_view(), name="admin/create-service"),
    path("update/<int:pk>/", view=UpdateServiceView.as_view(), name="admin/update-service"),
    path("delete/<int:pk>/", view=DeleteServiceView.as_view(), name="admin/delete-service"),
    
]