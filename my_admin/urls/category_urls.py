from django.urls import path

from my_admin.views.category_views import *

categories_patterns = [
    path("", view=ListCategoryView.as_view(), name="admin/list-category"),
    path("create/", view=CreateCategoryView.as_view(), name="admin/create-category"),
    path("update/<int:pk>/", view=UpdateCategoryView.as_view(), name="admin/update-category"),
    path("delete/<int:pk>/", view=DeleteCategoryView.as_view(), name="admin/delete-category"),
]