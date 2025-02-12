from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Service, Quote, Booking

# Create your views here.

class ListServiceView(ListView):
    model = Service
    template_name = 'services/list-services.html'


class DetailServiceView(DetailView):
    model = Service
    template_name = 'services/view-service.html'

@login_required
def add_quote(request):

    if request.POST:
        user = request.user
        service = Service.objects.get(id=request.POST['service_id'])
        description = request.POST["description"]
        Quote.objects.create(user=user, service=service, description=description)

    
    return redirect("list-services")

@login_required
def view_bookings(request):

    bookings = Booking.objects.filter(user=request.user)

    context = {
        "bookings": bookings
    }

    return render(request, "services/bookings.html", context)


class BookingDetail(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = "services/booking-detail.html"