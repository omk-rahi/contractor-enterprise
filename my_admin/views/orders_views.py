from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from shop.models import Order

# Create your views here.


class ListOrderView(AddExtraContextMixin, ListView):
    model = Order
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    extra_context = {
        "title": "Orders",
        "fields": [field.name for field in Order._meta.get_fields() if not field.is_relation]
    }


# class CreateBrandView(AddExtraContextMixin, CreateView):
#     model = Brand
#     template_name = "my_admin/create-template.html"
#     fields = "__all__"
#     success_url = reverse_lazy('admin/list-brand')

#     extra_context = {
#         "title": "Brand"
#     }

# class UpdateBrandView(AddExtraContextMixin, UpdateView):
#     model = Brand
#     template_name = "my_admin/update-template.html"
#     fields = "__all__"
#     success_url = reverse_lazy('admin/list-brand')

#     extra_context = {
#         "title": "Brand"
#     }

# class DeleteBrandView(AddExtraContextMixin, DeleteView):
#     model = Brand
#     template_name = "my_admin/delete-template.html"
#     success_url = reverse_lazy('admin/list-brand')

#     extra_context = {
#         "title": "Brand"
#     }
