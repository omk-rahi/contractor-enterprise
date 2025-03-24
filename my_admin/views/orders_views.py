from django.views.generic import  UpdateView, View, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from my_admin.utils import AddExtraContextMixin
from shop.models import Order, Warranty

# Create your views here.


class ListOrderView(View):
    def get(self, request):

        object_list = Order.objects.filter()
        

        extra = {
            "title": "Orders",
            "fields" : ["id", "status", "date", "total", 'item_description'],
            "disable_create": True,
            "disable_delete": True,
            "allow_view_detail": True
        }

        return render(request, "my_admin/list-template.html", context={"object_list": object_list, "extra" : extra}) 



class OrderDetailView(AddExtraContextMixin, DetailView):
    model = Order
    template_name = "my_admin/order-detail.html"

    extra_context = {
        "disable_create": True,
        "title": "Order Detail",
    }


class UpdateOrderView(AddExtraContextMixin, UpdateView):
    model = Order
    template_name = "my_admin/update-template.html"
    fields = ['status']
    success_url = reverse_lazy('admin/list-order')

    extra_context = {
        "disable_create": True,
        "title": "Update Order"
    }

    def form_valid(self, form):
        response = super().form_valid(form)
        order = form.instance  

        if order.status.lower() == "delivered":
            order.payment.status = "completed"
            order.payment.save(update_fields=["status"])

            for item in order.items.all():
                    Warranty.objects.create(order_item=item)


        return response