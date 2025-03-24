from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, UpdateView
from my_admin.utils import AddExtraContextMixin
from shop.models import CustomPCBuild, Warranty



class ListCustomOrderView(View):
    def get(self, request):
        object_list = CustomPCBuild.objects.all()

        extra = {
            "title": "Custom Orders",
            "fields": ["id", "status", "total_price", "created_at"],
            "disable_create": True,
            "disable_delete": True,
            "allow_view_detail": True
        }

        return render(request, "my_admin/list-template.html", context={"object_list": object_list, "extra": extra})


class CustomOrderDetailView(AddExtraContextMixin, DetailView):
    model = CustomPCBuild
    template_name = "my_admin/custom-order-detail.html"

    extra_context = {
        "disable_create": True,
        "title": "Custom Order Detail",
    }


class UpdateCustomOrderView(AddExtraContextMixin, UpdateView):
    model = CustomPCBuild
    template_name = "my_admin/update-template.html"
    fields = ["status"]
    success_url = reverse_lazy("admin/list-custom-order")

    extra_context = {
        "disable_create": True,
        "title": "Update Custom Order"
    }

    def form_valid(self, form):
        response = super().form_valid(form)
        order = form.instance  

        if order.status.lower() == "delivered":
            order.payment.status = "completed"
            order.payment.save(update_fields=["status"])

            for item in order.pcbuilditem_set.all():  
                Warranty.objects.create(order_item=item)

        return response
