from django.urls import path

from .views import ListServiceView, DetailServiceView, add_quote, view_bookings, BookingDetail

urlpatterns = [
    path('', ListServiceView.as_view(), name="list-services"),
    path('<int:pk>/', DetailServiceView.as_view(), name="view-service"),
    path('submit-quote/', add_quote, name="add-quote"),
    path("bookings/", view_bookings, name="list-bookings"),
    path("bookings/<int:pk>/", BookingDetail.as_view(), name="view-booking")
]
