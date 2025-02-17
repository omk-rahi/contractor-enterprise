from django.urls import path, include
from my_admin.views.products_views import *
from my_admin.views.product_images_views import *
from my_admin.views.product_specs_views import *
from my_admin.views.product_stock_views import *


product_image_patterns = [
    path("", ListProductImageView.as_view(), name="admin/list-product-image"),
    path("create", CreateProductImageView.as_view(), name="admin/create-product-image"),
    path("update/<int:pk>/", UpdateProductImageView.as_view(), name="admin/update-product-image"),
    path("delete/<int:pk>/", DeleteProductImageView.as_view(), name="admin/delete-product-image"),
]

product_spec_patterns = [
    path("", ListProductSpecsView.as_view(), name="admin/list-product-spec"),
    path("create", CreateProductSpecsView.as_view(), name="admin/create-product-spec"),
    path("update/<int:pk>/", UpdateProductSpecsView.as_view(), name="admin/update-product-spec"),
    path("delete/<int:pk>/", DeleteProductSpecsView.as_view(), name="admin/delete-product-spec"),
]



product_stock_patterns = [
    path("", ListProductStockView.as_view(), name="admin/list-product-stock"),
    path("create", CreateProductStockView.as_view(), name="admin/create-product-stock"),
    path("update/<int:pk>/", UpdateProductStockView.as_view(), name="admin/update-product-stock"),
    path("delete/<int:pk>/", DeleteProductStockView.as_view(), name="admin/delete-product-stock"),
]




product_patterns = [
    path("", ListProductView.as_view(), name="admin/list-product"),
    path("<int:product_pk>/", DetailProductView.as_view(), name="admin/detail-product"),
    path("create/", view=CreateProductView.as_view(), name="admin/create-product"),
    path("update/<int:pk>/", view=UpdateProductView.as_view(), name="admin/update-product"),
    path("delete/<int:pk>/", view=DeleteProductView.as_view(), name="admin/delete-product"),
    path("<int:product_pk>/images/", include(product_image_patterns)),
    path("<int:product_pk>/specs/", include(product_spec_patterns)),
    path("<int:product_pk>/stock/", include(product_stock_patterns)),
]
