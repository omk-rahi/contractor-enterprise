from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from services.models import Service, ServiceCost

# Create your views here.


class ListServiceCostView(AddExtraContextMixin, ListView):
    model = ServiceCost
    template_name = "my_admin/list-template.html"
    paginate_by = 5
    ordering = ['id']
    extra_context = {
        "title": "Service Costs",
        "fields": [field.name for field in ServiceCost._meta.get_fields() if not field.is_relation]
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(service=self.kwargs.get('pk'))


class CreateServiceCostView(AddExtraContextMixin, CreateView):
    model = ServiceCost
    template_name = "my_admin/create-template.html"
    fields = "__all__"

    extra_context = {
        "title": "Add Service Cost"
    }

    def get_initial(self):
        initial = super().get_initial()

        initial["service"] = Service.objects.get(id=self.kwargs['service_pk'])

        return initial

    def get_success_url(self):
        return reverse_lazy('admin/list-service-cost', kwargs={'pk': self.kwargs["service_pk"]})

class UpdateServiceCostView(AddExtraContextMixin, UpdateView):
    model = ServiceCost
    template_name = "my_admin/update-template.html"
    fields = "__all__"

    extra_context = {
        "title": "Update Service Cost"
    }

    def get_success_url(self):
        return reverse_lazy('admin/list-service-cost', kwargs={'pk': self.kwargs["service_pk"]})

class DeleteServiceCostView(AddExtraContextMixin, DeleteView):
    model = ServiceCost
    template_name = "my_admin/delete-template.html"

    extra_context = {
        "title": "Delete Service Cost"
    }

    def get_success_url(self):
        return reverse_lazy('admin/list-service-cost', kwargs={'pk': self.kwargs["service_pk"]})