from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from shop.models import Product, ProductSpec, Specification
from shop.forms import UpdateProductSpecForm

# Create your views here.

class ListProductSpecsView(AddExtraContextMixin, ListView):
    model = ProductSpec
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    ordering = ['id']
    extra_context = {
        "title": "Product Specs",
        "fields": [field.name for field in ProductSpec._meta.get_fields() if not field.is_relation]
    }

    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(product=self.kwargs.get('product_pk'))


class CreateProductSpecsView(AddExtraContextMixin, CreateView):
    model = ProductSpec
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    

    extra_context = {
        "title": "Add New Product Specs"
    }

    def get_initial(self):
        initial = super().get_initial()

        initial["product"] = Product.objects.get(id = self.kwargs["product_pk"])

        return initial
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        product = Product.objects.get(id = self.kwargs["product_pk"])
        form.fields["specification"].queryset = Specification.objects.filter(category=product.category)
        return form

    def get_success_url(self):
        return reverse_lazy('admin/list-product-spec', kwargs={'product_pk': self.kwargs["product_pk"]})
    
    
class UpdateProductSpecsView(AddExtraContextMixin, UpdateView):
    model = ProductSpec
    template_name = "my_admin/update-template.html"
    form_class = UpdateProductSpecForm
    extra_context = {
        "title": "Update Product Specs"
    }
    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-spec', kwargs={'product_pk': self.kwargs["product_pk"]})
    

class DeleteProductSpecsView(AddExtraContextMixin, DeleteView):
    model = ProductSpec
    template_name = "my_admin/delete-template.html"

    extra_context = {
        "title": "Delete Product Specs"
    }

    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-spec', kwargs={'product_pk': self.kwargs["product_pk"]})

