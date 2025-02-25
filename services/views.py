from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from my_admin.utils import AddExtraContextMixin

from .models import Service, Quote, Booking, ServiceCost

from .forms import NewQuoteForm

# Create your views here.

class ListServiceView(ListView):
    model = Service
    template_name = 'services/list-services.html'


class DetailServiceView(AddExtraContextMixin, DetailView):
    model = Service
    template_name = 'services/view-service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.get_object()        
        context["form"] = NewQuoteForm(service=service)
        return context

@login_required
def add_quote(request):

    if request.POST:
        user = request.user

        if user.address.address_line == "":
            messages.error(request, "Please add your address first")
            return redirect("user-settings")

        service = Service.objects.get(id=request.POST['service_id'])
        description = request.POST["description"]
        problem = request.POST["problem"]
        cost = get_object_or_404(ServiceCost, pk=problem)
        Quote.objects.create(user=user, service=service, description=description, problem=cost)

        messages.success(request, "Quote added. We will contact you later")

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