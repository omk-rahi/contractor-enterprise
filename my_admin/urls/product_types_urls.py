from django.urls import path

from my_admin.views.product_type_views import *

product_types_patterns = [
    path("", ListProductTypeView.as_view(), name="admin/list-product-type"),
    path("create/", view=CreateProductTypeView.as_view(), name="admin/create-product-type"),
    path("update/<int:pk>/", view=UpdateProductTypeView.as_view(), name="admin/update-product-type"),
    path("delete/<int:pk>/", view=DeleteProductTypeView.as_view(), name="admin/delete-product-type"),
]