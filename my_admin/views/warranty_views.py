from django.views.generic import View, ListView, DetailView, UpdateView
from my_admin.utils import AddExtraContextMixin

from django.shortcuts import render
from django.urls import reverse_lazy
from shop.models import Warranty, WarrantyClaim

class ListWarrantyView(View):
    def get(self, request):
        object_list = Warranty.objects.all()

        extra = {
            "title": "Warranties",
            "fields": ["id", "order_item", "warranty_start_date", "warranty_end_date"],
            "disable_create": True,
            "disable_delete": True,
            "disable_update": True,
            "allow_view_detail": True,

        }

        return render(request, "my_admin/list-template.html", context={"object_list": object_list, "extra": extra})
    
class DetailWarrantyView(DetailView):
    model = Warranty
    template_name = "my_admin/warranty-detail.html"
    context_object_name = "warranty"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        warranty = self.object
        order_item = warranty.order_item
        order = order_item.order
        customer = order.user

        context["extra"] = {
            "title": f"Warranty Details for {order_item.product.name}",
            "disable_create": True,
            "fields": [
                ("Warranty ID", warranty.id),
                ("Product", order_item.product.name),
                ("Order ID", order.id),
                ("Order Status", order.status),
                ("Start Date", warranty.warranty_start_date),
                ("End Date", warranty.warranty_end_date),
                ("Valid", "Yes" if warranty.is_valid() else "No"),
            ],
            "customer": {
                "Customer Name": customer.get_full_name(),
                "Email": customer.email,
                "Phone": customer.phone,
                "Address": f"{customer.address}" if hasattr(customer, 'address') else "N/A",
            },
        }
        return context
    

class ListWarrantyClaimView(AddExtraContextMixin, ListView):
    model = WarrantyClaim
    template_name = "my_admin/list-template.html"
    paginate_by = 5
    ordering = ['-submitted_at']
    extra_context = {
        "title": "Warranty Claims",
        "fields": ["id", "order_item", "claim_reason", "status", "user", "submitted_at"],
        "disable_create": True,
        "disable_delete": True,
        "allow_view_detail": True,
    }

class WarrantyClaimDetailView(DetailView):
    model = WarrantyClaim
    template_name = "my_admin/warranty_claim_detail.html"
    context_object_name = "claim"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        claim = self.object
        order_item = claim.order_item

        context["extra"] = {
            "title": f"Claim Details for {order_item.product.name}",
            "disable_create": True,
        }
        return context
  

class WarrantyClaimUpdateView(UpdateView):
    model = WarrantyClaim
    fields = ["status", "admin_remark"]
    template_name = "my_admin/update-template.html"
    success_url = reverse_lazy("admin/list-claims")