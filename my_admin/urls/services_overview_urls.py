from django.urls import path, include

from my_admin.views.services_views import ServicesOverview

from .services_urls import services_patterns
from .quotes_urls import quote_patterns
from .booking_urls import bookings_patterns
from .feedback_urls import feedback_patterns

services_overview_patterns = [
    path("", view=ServicesOverview.as_view(), name="admin/services-overview"),
    path("services/", include(services_patterns)),
    path("quotes/", include(quote_patterns)),
    path("bookings/", include(bookings_patterns)),
    path("feedbacks/", include(feedback_patterns))
    
]