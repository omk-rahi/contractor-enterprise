from django.urls import path, include

from my_admin.views import ShopOverview
from my_admin.views.category_views import *

from .brands_urls import brands_patterns
from .category_urls import categories_patterns
from .product_urls import product_patterns
from .spec_urls import spec_patterns
shop_patterns = [
    path("", view=ShopOverview.as_view(), name="admin/shop-overview"),
    path('brands/', include(brands_patterns)),
    path('categories/', include(categories_patterns)),
    path('products/', include(product_patterns)),
    path('specs/', include(spec_patterns)),
    
]