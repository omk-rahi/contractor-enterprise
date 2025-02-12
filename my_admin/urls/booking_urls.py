from django.urls import path

from my_admin.views.bookings_views import *

bookings_patterns = [
    path("", ListBookingView.as_view(), name="admin/list-booking"),
    path("<int:pk>/", view=BookingDetailView.as_view(), name="admin/view-booking"),
    path("create/", view=CreateBookingView.as_view(), name="admin/create-booking"),
    path("update/<int:pk>", view=UpdateBookingView.as_view(), name="admin/update-booking"),
    path("delete/<int:pk>", view=DeleteBookingView.as_view(), name="admin/delete-booking"),
]