from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from django.shortcuts import render
from accounts.models import CustomUser
from accounts.forms import StaffRegisterForm


# Create your views here.


class ListStaffView(View):
    def get(self, request):

        object_list = CustomUser.objects.filter(role='staff')

        extra = {
            "title": "Staffs",
            "fields" : ["id", "fullname", "email", "phone"],
        }

        return render(request, "my_admin/list-template.html", context={"object_list": object_list, "extra" : extra}) 


class CreateStaffView(AddExtraContextMixin, CreateView):
    model = CustomUser
    form_class = StaffRegisterForm
    template_name = "my_admin/create-template.html"
    success_url = reverse_lazy('admin/list-staff')

    extra_context = {
        "title": "Staff"
    }

class UpdateStaffView(AddExtraContextMixin, UpdateView):
    model = CustomUser
    template_name = "my_admin/update-template.html"
    form_class = StaffRegisterForm
    success_url = reverse_lazy('admin/list-staff')

    extra_context = {
        "title": "Staff"
    }

class DeleteStaffView(AddExtraContextMixin, DeleteView):
    model = CustomUser
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-staff')

    extra_context = {
        "title": "Staff"
    }
