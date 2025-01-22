from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from services.models import Service

# Create your views here.

class ServicesOverview(TemplateView):
    template_name = "my_admin/services-overview.html"
    

class ListServiceView(AddExtraContextMixin, ListView):
    model = Service
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    extra_context = {
        "title": "Services",
        "fields": [field.name for field in Service._meta.get_fields() if not field.is_relation]
    }


class CreateServiceView(AddExtraContextMixin, CreateView):
    model = Service
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-service')

    extra_context = {
        "title": "Service"
    }

class UpdateServiceView(AddExtraContextMixin, UpdateView):
    model = Service
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-service')

    extra_context = {
        "title": "Service"
    }

class DeleteServiceView(AddExtraContextMixin, DeleteView):
    model = Service
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-service')

    extra_context = {
        "title": "Service"
    }
