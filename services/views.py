from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Service, Booking, ServiceCost

from .forms import QuoteForm

# Create your views here.

class ListServiceView(ListView):
    model = Service
    template_name = 'services/list-services.html'


def service_detail(request, pk):
    service = get_object_or_404(Service, id=pk)
    return render(request, "services/view-service.html", {"service": service})


@login_required
def get_quote(request, pk):
    service = get_object_or_404(Service, id=pk)

    form = QuoteForm()

    form.fields["problems"].queryset = ServiceCost.objects.filter(service=service)

    if request.method == "POST":
        form = QuoteForm(request.POST)
        form.fields["problems"].queryset = ServiceCost.objects.filter(service=service)

        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.service = service
            quote.save()
            form.save_m2m()
            messages.success(request, "Your quote request has been submitted!")
            return redirect("view-service", pk=pk)
        else:
            print(form.errors) 

    return render(request, "services/get_quote.html", {"service": service, "form": form})

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

