from django.urls import path, include
# from django.views.generic.edit import UpdateView

# from . import forms

from . import views


brands_patterns = [
    path("", views.ListBrandView.as_view(), name="admin/list-brand"),
    path("create/", view=views.CreateBrandView.as_view(), name="admin/create-brand"),
    path("update/<int:pk>/", view=views.UpdateBrandView.as_view(), name="admin/update-brand"),
    path("delete/<int:pk>/", view=views.DeleteBrandView.as_view(), name="admin/delete-brand"),
]

product_types_patterns = [
    path("", views.ListProductTypeView.as_view(), name="admin/list-product-type"),
    path("create/", view=views.CreateProductTypeView.as_view(), name="admin/create-product-type"),
    path("update/<int:pk>/", view=views.UpdateProductTypeView.as_view(), name="admin/update-product-type"),
    path("delete/<int:pk>/", view=views.DeleteProductTypeView.as_view(), name="admin/delete-product-type"),
]

categories_patterns = [
    path("", views.ListCategoryView.as_view(), name="admin/list-category"),
    path("create/", view=views.CreateCategoryView.as_view(), name="admin/create-category"),
    path("update/<int:pk>/", view=views.UpdateCategoryView.as_view(), name="admin/update-category"),
    path("delete/<int:pk>/", view=views.DeleteCategoryView.as_view(), name="admin/delete-category"),
]

product_patterns = [
    path("", views.ListProductView.as_view(), name="admin/list-product"),
    path("<int:pk>/", views.DetailProductView.as_view(), name="admin/detail-product"),
    path("create/", view=views.CreateProductView.as_view(), name="admin/create-product"),
    path("update/<int:pk>/", view=views.UpdateProductView.as_view(), name="admin/update-product"),
    path("delete/<int:pk>/", view=views.DeleteProductView.as_view(), name="admin/delete-product"),
    path("<int:product_pk>/images/", views.ListProductImageView.as_view(), name="admin/list-product-image"),
    path("<int:product_pk>/images/create", views.CreateProductImageView.as_view(), name="admin/create-product-image"),
    path("<int:product_pk>/images/update/<int:pk>/", views.UpdateProductImageView.as_view(), name="admin/update-product-image"),
    path("<int:product_pk>/images/delete/<int:pk>/", views.DeleteProductImageView.as_view(), name="admin/delete-product-image"),
    path("<int:product_pk>/specs/", views.ListProductSpecsView.as_view(), name="admin/list-product-spec"),
    path("<int:product_pk>/specs/create", views.CreateProductSpecsView.as_view(), name="admin/create-product-spec"),
    path("<int:product_pk>/specs/update/<int:pk>/", views.UpdateProductSpecsView.as_view(), name="admin/update-product-spec"),
    path("<int:product_pk>/specs/delete/<int:pk>/", views.DeleteProductSpecsView.as_view(), name="admin/delete-product-spec"),
]



shop_patterns = [
    path("", view=views.ShopOverview.as_view(), name="admin/shop-overview"),
    path('brands/', include(brands_patterns)),
    path('product-types/', include(product_types_patterns)),
    path('categories/', include(categories_patterns)),
    path('products/', include(product_patterns)),
    
]


services_patterns = [
    path("", views.ListServiceView.as_view(), name="admin/list-service"),
    path("create/", view=views.CreateServiceView.as_view(), name="admin/create-service"),
    path("update/<int:pk>/", view=views.UpdateServiceView.as_view(), name="admin/update-service"),
    path("delete/<int:pk>/", view=views.DeleteServiceView.as_view(), name="admin/delete-service"),
    
]

staff_patterns = [
    path("", views.ListStaffView.as_view(), name="admin/list-staff"),
    path("create/", view=views.CreateStaffView.as_view(), name="admin/create-staff"),
    path("update/<int:pk>/", view=views.UpdateStaffView.as_view(), name="admin/update-staff"),
    path("delete/<int:pk>/", view=views.DeleteStaffView.as_view(), name="admin/delete-staff"),
    
]



urlpatterns = [
    path("", view=views.DashBoardView.as_view(), name="admin/dashboard"),
    path("services-overview/", view=views.ServicesOverview.as_view(), name="admin/services-overview"),
    path("services/", include(services_patterns)),
    path("shop/", include(shop_patterns)),
    path("customers/", view=views.ListCustomerView.as_view(), name="admin/list-customer"),
    path("staffs/",include(staff_patterns)),
    path("settings/",view=views.UpdateAdminView.as_view(), name="admin/settings"),
]
