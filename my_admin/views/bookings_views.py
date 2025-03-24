from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from django.db.models import Prefetch
from services.models import Booking, ServiceCost
from services.forms import UpdateBookingForm


class ListBookingView(AddExtraContextMixin, ListView):
    model = Booking
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    ordering = ['id']
    extra_context = {
        "title": "Bookings",
        "fields": [field.name for field in Booking._meta.get_fields() if not field.is_relation],
        "allow_view_detail": True
    }

class CreateBookingView(AddExtraContextMixin, CreateView):
    model = Booking
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-booking')

    extra_context = {
        "title": "Add New Booking"
    }

class DeleteBookingView(AddExtraContextMixin, DeleteView):
    model = Booking
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-booking')

    extra_context = {
        "title": "Delete Booking"
    }

class BookingDetailView(AddExtraContextMixin, DetailView):
    model = Booking
    template_name = "my_admin/booking-detail.html"

    extra_context = {
        "disable_create": True,
        "title": "Booking Detail",
    }

class UpdateBookingView(AddExtraContextMixin, UpdateView):
    model = Booking
    template_name = "my_admin/update-template.html"
    success_url = reverse_lazy('admin/list-booking')

    form_class = UpdateBookingForm

    extra_context = {
        "title": "Update Booking"
    }

