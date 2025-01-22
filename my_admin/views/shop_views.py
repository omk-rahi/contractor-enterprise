from django.views.generic import TemplateView

class ShopOverview(TemplateView):
    template_name = "my_admin/shop-overview.html"