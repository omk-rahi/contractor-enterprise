from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from shop.models import ProductType

# Create your views here.

class ListProductTypeView(AddExtraContextMixin, ListView):
    model = ProductType
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    ordering = ['id']
    extra_context = {
        "title": "Product Types",
        "fields": [field.name for field in ProductType._meta.get_fields() if not field.is_relation]
    }


class CreateProductTypeView(AddExtraContextMixin, CreateView):
    model = ProductType
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-product-type')

    extra_context = {
        "title": "Add New Product Type"
    }

class UpdateProductTypeView(AddExtraContextMixin, UpdateView):
    model = ProductType
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-product-type')

    extra_context = {
        "title": "Update Product Type"
    }

class DeleteProductTypeView(AddExtraContextMixin, DeleteView):
    model = ProductType
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-product-type')

    extra_context = {
        "title": "Delete Product Type"
    }
