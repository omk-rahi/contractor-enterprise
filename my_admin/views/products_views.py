from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from shop.models import Product, ProductImage, Specification, ProductStock

# Create your views here.

class ListProductView(AddExtraContextMixin, ListView):
    model = Product
    template_name = "my_admin/list-template.html"
    paginate_by = 3 
    ordering = ['id']
    extra_context = {
        "title": "Products",
        "fields": [field.name for field in Product._meta.get_fields() if not field.is_relation],
        "allow_view_detail": True
    }


class DetailProductView(AddExtraContextMixin, View):

    def get(self, request, product_pk):

        template_name = "my_admin/product-detail.html"
        object = Product.objects.get(id=product_pk)
        

        extra_context = {
            "image_count": ProductImage.objects.filter(product=object.id).count(),
            "stock_count": ProductStock.objects.filter(product=object.id, status="available").count(),
            "specs_count": 0,
            "reviews_count": 0,
            "title": object.name
        }

        return render(request, template_name=template_name, context={"object": object, "extra" : extra_context}) 




class CreateProductView(AddExtraContextMixin, CreateView):
    model = Product
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-product')

    extra_context = {
        "title": "Add New Product"
    }

class UpdateProductView(AddExtraContextMixin, UpdateView):
    model = Product
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-product')

    extra_context = {
        "title": "Update Product"
    }

class DeleteProductView(AddExtraContextMixin, DeleteView):
    model = Product
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-product')

    extra_context = {
        "title": "Delete Product"
    }

