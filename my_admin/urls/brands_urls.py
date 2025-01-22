from django.urls import path

from my_admin.views.brands_views import *

brands_patterns = [
    path("", ListBrandView.as_view(), name="admin/list-brand"),
    path("create/", view=CreateBrandView.as_view(), name="admin/create-brand"),
    path("update/<int:pk>/", view=UpdateBrandView.as_view(), name="admin/update-brand"),
    path("delete/<int:pk>/", view=DeleteBrandView.as_view(), name="admin/delete-brand"),
]