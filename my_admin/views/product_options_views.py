from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from shop.models import Product, ProductOption

# Create your views here.

class ListProductOptionsView(AddExtraContextMixin, ListView):
    model = ProductOption
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    ordering = ['id']
    extra_context = {
        "title": "Product Options",
        "fields": [field.name for field in ProductOption._meta.get_fields() if not field.is_relation]
    }


class CreateProductOptionsView(AddExtraContextMixin, CreateView):
    model = ProductOption
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    

    extra_context = {
        "title": "Product Option"
    }

    def get_initial(self):
        initial = super().get_initial()

        initial["product"] = self.kwargs["product_pk"]

        return initial
    
    
    def form_valid(self, form):
        
        form.instance.product = Product.objects.get(id = self.kwargs["product_pk"])

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-option', kwargs={'product_pk': self.kwargs["product_pk"]})
    
    
class UpdateProductOptionsView(AddExtraContextMixin, UpdateView):
    model = ProductOption
    template_name = "my_admin/update-template.html"
    fields = "__all__"

    extra_context = {
        "title": "Product Option"
    }

    def get_initial(self):
        initial = super().get_initial()

        initial["product"] = self.kwargs["product_pk"]

        return initial
    
    
    def form_valid(self, form):
        
        form.instance.product = Product.objects.get(id = self.kwargs["product_pk"])

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-option', kwargs={'product_pk': self.kwargs["product_pk"]})
    

class DeleteProductOptionsView(AddExtraContextMixin, DeleteView):
    model = ProductOption
    template_name = "my_admin/delete-template.html"

    extra_context = {
        "title": "Product Option"
    }

    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-option', kwargs={'product_pk': self.kwargs["product_pk"]})

