from django.shortcuts import redirect, render
from django.views.generic import ListView
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
        "fields": ["id", "description", "status", "service", "user", "user_phone", "user_address"],
        "disable_create": True,
        "disable_delete": True,
    }


def UpdateQuote(request, pk):
    
    item = Quote.objects.get(id=pk)
    
    if request.POST:

        form = UpdateQuoteForm(request.POST, instance=item)

        status = request.POST['status']

        if status == 'rejected':
            item.delete()
            return redirect("admin/list-quote")
        
        if status == "approved":
            Booking.objects.create(service=item.service, user=item.user, cost=request.POST['estimated_cost'], additional_note=item.description)
            item.delete()
            return redirect("admin/list-quote")

        if form.is_valid():
            form.save()

            return redirect("admin/list-quote")

    else:
        form = UpdateQuoteForm(instance=item)

        return render(request, 'my_admin/update-template.html', {"form": form})
        