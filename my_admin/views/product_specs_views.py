from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from shop.models import Product, Specification

# Create your views here.

class ListProductSpecsView(AddExtraContextMixin, ListView):
    model = Specification
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    extra_context = {
        "title": "Product Specs",
        "fields": [field.name for field in Specification._meta.get_fields() if not field.is_relation]
    }


class CreateProductSpecsView(AddExtraContextMixin, CreateView):
    model = Specification
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    

    extra_context = {
        "title": "Product Specs"
    }

    def get_initial(self):
        initial = super().get_initial()

        initial["product"] = self.kwargs["product_pk"]

        return initial
    
    
    def form_valid(self, form):
        
        form.instance.product = Product.objects.get(id = self.kwargs["product_pk"])

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-spec', kwargs={'product_pk': self.kwargs["product_pk"]})
    
    
class UpdateProductSpecsView(AddExtraContextMixin, UpdateView):
    model = Specification
    template_name = "my_admin/update-template.html"
    fields = "__all__"

    extra_context = {
        "title": "Product Specs"
    }

    def get_initial(self):
        initial = super().get_initial()

        initial["product"] = self.kwargs["product_pk"]

        return initial
    
    
    def form_valid(self, form):
        
        form.instance.product = Product.objects.get(id = self.kwargs["product_pk"])

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-spec', kwargs={'product_pk': self.kwargs["product_pk"]})
    

class DeleteProductSpecsView(AddExtraContextMixin, DeleteView):
    model = Specification
    template_name = "my_admin/delete-template.html"

    extra_context = {
        "title": "Product Specs"
    }

    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-spec', kwargs={'product_pk': self.kwargs["product_pk"]})

