from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from my_admin.utils import AddExtraContextMixin
from services.models import Feedback

# Create your views here.

class ListFeedbackView(AddExtraContextMixin, ListView):
    model = Feedback
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    ordering = ['id']
    extra_context = {
        "title": "Feedbacks",
        "fields": ["id", "service", "comment", "user"],
        "disable_action": True,
        "disable_create": True,
    }
