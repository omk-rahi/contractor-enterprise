from django.urls import path

from my_admin.views.spec_views import *

spec_patterns = [
    path("", ListSpecView.as_view(), name="admin/list-spec"),
    path("create/", view=CreateSpecView.as_view(), name="admin/create-spec"),
    path("update/<int:pk>/", view=UpdateSpecView.as_view(), name="admin/update-spec"),
    path("delete/<int:pk>/", view=DeleteSpecView.as_view(), name="admin/delete-spec"),
]