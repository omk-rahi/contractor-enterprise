from django.urls import path

from my_admin.views.feedback_views import *

feedback_patterns = [
    path("", ListFeedbackView.as_view(), name="admin/list-feedback"),
]