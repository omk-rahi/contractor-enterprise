from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from services.models import Service, Quote, Booking

# Create your views here.

class ServicesOverview(AddExtraContextMixin, View):

    def get(self, request):

        template_name = "my_admin/services-overview.html"

        extra_context = {
            "services_count": Service.objects.all().count(),
            "quotes_count": Quote.objects.all().count(),
            "bookings_count": Booking.objects.count(),
            "disable_create": True,
            "title": "Services Overview",

        }

        return render(request, template_name=template_name, context={"extra" : extra_context}) 

        

class ListServiceView(AddExtraContextMixin, ListView):
    model = Service
    template_name = "my_admin/list-template.html"
    paginate_by = 5
    ordering = ['id']
    extra_context = {
        "title": "Services",
        "fields": [field.name for field in Service._meta.get_fields() if not field.is_relation],
        "allow_view_detail": True

    }


class CreateServiceView(AddExtraContextMixin, CreateView):
    model = Service
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-service')

    extra_context = {
        "title": "Add New Service"
    }

class UpdateServiceView(AddExtraContextMixin, UpdateView):
    model = Service
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-service')

    extra_context = {
        "title": "Update Service"
    }

class DeleteServiceView(AddExtraContextMixin, DeleteView):
    model = Service
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-service')

    extra_context = {
        "title": "Delete Service"
    }
