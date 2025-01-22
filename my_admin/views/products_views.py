from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from shop.models import Product

# Create your views here.

class ListProductView(AddExtraContextMixin, ListView):
    model = Product
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    extra_context = {
        "title": "Products",
        "fields": [field.name for field in Product._meta.get_fields() if not field.is_relation],
        "allow_view_detail": True
    }


class DetailProductView(AddExtraContextMixin, DetailView):
    model = Product
    template_name = "my_admin/product-detail.html"



class CreateProductView(AddExtraContextMixin, CreateView):
    model = Product
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-product')

    extra_context = {
        "title": "Product"
    }

class UpdateProductView(AddExtraContextMixin, UpdateView):
    model = Product
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-product')

    extra_context = {
        "title": "Product"
    }

class DeleteProductView(AddExtraContextMixin, DeleteView):
    model = Product
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-product')

    extra_context = {
        "title": "Product"
    }

