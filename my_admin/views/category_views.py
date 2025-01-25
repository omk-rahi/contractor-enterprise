from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from shop.models import Category

# Create your views here.

class ListCategoryView(AddExtraContextMixin, ListView):
    model = Category
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    ordering = ['id']
    extra_context = {
        "title": "Categories",
        "fields": [field.name for field in Category._meta.get_fields() if not field.is_relation]
    }


class CreateCategoryView(AddExtraContextMixin, CreateView):
    model = Category
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-category')

    extra_context = {
        "title": "Category"
    }

class UpdateCategoryView(AddExtraContextMixin, UpdateView):
    model = Category
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-category')

    extra_context = {
        "title": "Category"
    }

class DeleteCategoryView(AddExtraContextMixin, DeleteView):
    model = Category
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-category')

    extra_context = {
        "title": "Category"
    }
