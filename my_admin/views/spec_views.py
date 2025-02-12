from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from shop.models import Specification

# Create your views here.


class ListSpecView(AddExtraContextMixin, ListView):
    model = Specification
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    ordering = ['id']
    extra_context = {
        "title": "Specifications",
        "fields": ['id', 'key', 'category']
    }


class CreateSpecView(AddExtraContextMixin, CreateView):
    model = Specification
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-spec')

    extra_context = {
        "title": "Add New Specification"
    }

class UpdateSpecView(AddExtraContextMixin, UpdateView):
    model = Specification
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-spec')

    extra_context = {
        "title": "Update Specification"
    }

class DeleteSpecView(AddExtraContextMixin, DeleteView):
    model = Specification
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-spec')

    extra_context = {
        "title": "Delete Specification"
    }
