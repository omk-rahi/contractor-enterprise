from django.views.generic import  TemplateView, UpdateView
from django.urls import reverse_lazy
from my_admin.utils import AddExtraContextMixin
from accounts.models import CustomUser


# Create your views here.

class DashBoardView(TemplateView):
    template_name = "my_admin/dashboard.html"

class UpdateAdminView(AddExtraContextMixin, UpdateView):
    model = CustomUser
    template_name = "my_admin/update-template.html"
    fields = ["fullname", "email", "phone", "profile_image"]
    success_url = reverse_lazy('admin/dashboard')

    extra_context = {
        "title": "Settings"
    }

    def get_object(self):
        return self.request.user