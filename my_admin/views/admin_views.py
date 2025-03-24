from django.shortcuts import render
from django.views.generic import  View, UpdateView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from accounts.models import CustomUser
from shop.models import *

# Create your views here.

class DashBoardView(AddExtraContextMixin, View):

    def get(self, request):

        template_name = "my_admin/dashboard.html"

        extra_context = {
            "customer_count": CustomUser.objects.filter(role="customer").count(),
            "staff_count": CustomUser.objects.filter(role="staff").count(),
            "order_count": Order.objects.all().count(),
            "custom_order_count": CustomPCBuild.objects.all().count(),
            "warranty_count": Warranty.objects.all().count(),
            "claim_count": Warranty.objects.all().count(),
            "payment_count": Payment.objects.all().count(),
            "disable_create": True,
            "title": "Dashboard"
        }

        return render(request, template_name=template_name, context={"extra" : extra_context}) 


class UpdateAdminView(AddExtraContextMixin, UpdateView):
    model = CustomUser
    template_name = "my_admin/update-template.html"
    fields = ["fullname", "email", "phone", "profile_image"]
    success_url = reverse_lazy('admin/dashboard')

    extra_context = {
        "title": "Settings",
        "disable_create": True,
    }

    def get_object(self):
        return self.request.user