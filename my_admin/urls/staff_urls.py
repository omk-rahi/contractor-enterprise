from django.urls import path

from my_admin.views.staff_views import *


staff_patterns = [
    path("", ListStaffView.as_view(), name="admin/list-staff"),
    path("create/", view=CreateStaffView.as_view(), name="admin/create-staff"),
    path("update/<int:pk>/", view=UpdateStaffView.as_view(), name="admin/update-staff"),
    path("delete/<int:pk>/", view=DeleteStaffView.as_view(), name="admin/delete-staff"),
    
]