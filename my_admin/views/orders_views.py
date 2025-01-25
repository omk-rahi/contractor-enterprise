from django.views.generic import  UpdateView, View, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from my_admin.utils import AddExtraContextMixin
from shop.models import Order

# Create your views here.


class ListOrderView(View):
    def get(self, request):

        object_list = Order.objects.filter()
        

        extra = {
            "title": "Orders",
            "fields" : ["id", "status", "date", "total"],
            "disable_create": True,
            "disable_delete": True,
            "allow_view_detail": True
        }

        return render(request, "my_admin/list-template.html", context={"object_list": object_list, "extra" : extra}) 



class UpdateOrderView(AddExtraContextMixin, UpdateView):
    model = Order
    template_name = "my_admin/update-template.html"
    fields = ["status"]
    success_url = reverse_lazy('admin/list-order')

    extra_context = {
        "title": "Order"
    }


class OrderDetailView(DetailView):
    model = Order
    template_name = "my_admin/order-detail.html"