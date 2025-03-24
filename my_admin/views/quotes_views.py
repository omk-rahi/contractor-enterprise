from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from my_admin.utils import AddExtraContextMixin

from services.models import Quote, Booking
from services.forms import UpdateQuoteForm

# Create your views here.


class ListServiceQuoteView(AddExtraContextMixin, ListView):
    model = Quote
    template_name = "my_admin/list-template.html"
    paginate_by = 5
    ordering = ['id']
    extra_context = {
        "title": "Quotes",
        "fields": ["id", "description", "status", "service", "user", "user_phone"],
        "disable_create": True,
        "disable_delete": True,
        "allow_view_detail": True
    }

class DetailQuoteView(AddExtraContextMixin, DetailView):
    model = Quote
    template_name = "my_admin/quote-detail.html"
    context_object_name = "quote"

    extra_context = {
        "title": "Quote Detail",
        "disable_create": True,
    }


def UpdateQuote(request, pk):
    item = Quote.objects.get(id=pk)

    if request.method == "POST":
        form = UpdateQuoteForm(request.POST, instance=item)
        status = request.POST.get("status")

        if status == "rejected":
            item.delete()
            return redirect("admin/list-quote")

        if status == "approved":
            booking = Booking.objects.create(
                service=item.service,
                user=item.user,
                cost=request.POST.get("estimated_cost", 0),
                additional_note=item.description,
                status="created",
            )

            booking.problems.set(item.problems.all())

            item.delete()
            return redirect("admin/list-quote")

        if form.is_valid():
            form.save()
            return redirect("admin/list-quote")

    else:
        form = UpdateQuoteForm(instance=item)

    return render(request, "my_admin/update-template.html", {"form": form})

