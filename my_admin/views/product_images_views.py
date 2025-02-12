from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from shop.models import Product, ProductImage

# Create your views here.

class ListProductImageView(AddExtraContextMixin, ListView):
    model = ProductImage
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    ordering = ['id']
    extra_context = {
        "title": "Product Images",
        "fields": [field.name for field in ProductImage._meta.get_fields() if not field.is_relation]
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(product=self.kwargs.get('product_pk'))

    
    

class CreateProductImageView(AddExtraContextMixin, CreateView):
    model = ProductImage
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    

    extra_context = {
        "title": "Add New Product Image"
    }

    def get_initial(self):
        initial = super().get_initial()

        initial["product"] = Product.objects.get(id = self.kwargs["product_pk"])

        return initial
    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-image', kwargs={'product_pk': self.kwargs["product_pk"]})
    
    
class UpdateProductImageView(AddExtraContextMixin, UpdateView):
    model = ProductImage
    template_name = "my_admin/update-template.html"
    fields = "__all__"

    extra_context = {
        "title": "Update Product Image"
    }

    def get_success_url(self):
        return reverse_lazy('admin/list-product-image', kwargs={'product_pk': self.kwargs["product_pk"]})
    

class DeleteProductImageView(AddExtraContextMixin, DeleteView):
    model = ProductImage
    template_name = "my_admin/delete-template.html"

    extra_context = {
        "title": "Delete Product Image"
    }

    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-image', kwargs={'product_pk': self.kwargs["product_pk"]})
