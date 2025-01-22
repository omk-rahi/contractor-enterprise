from django.urls import path, include

from my_admin.views import ShopOverview
from my_admin.views.category_views import *

from .brands_urls import brands_patterns
from .product_types_urls import product_types_patterns
from .category_urls import categories_patterns
from .product_urls import product_patterns

shop_patterns = [
    path("", view=ShopOverview.as_view(), name="admin/shop-overview"),
    path('brands/', include(brands_patterns)),
    path('product-types/', include(product_types_patterns)),
    path('categories/', include(categories_patterns)),
    path('products/', include(product_patterns)),
    
]