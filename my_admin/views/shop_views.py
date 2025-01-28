from django.shortcuts import render
from django.views.generic import View
from my_admin.utils import AddExtraContextMixin
from shop.models import Product, Brand, ProductType, Category


class ShopOverview(AddExtraContextMixin, View):

    def get(self, request):

        template_name = "my_admin/shop-overview.html"

        extra_context = {
            "product_count": Product.objects.all().count(),
            "brand_count": Brand.objects.all().count(),
            "product_type_count": ProductType.objects.all().count(),
            "category_count": Category.objects.all().count(),
            "disable_create": True,
            "title": "Shop Overview"
        }

        return render(request, template_name=template_name, context={"extra" : extra_context}) 