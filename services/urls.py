from django.urls import path

from .views import *

urlpatterns = [
    path('', ListServiceView.as_view(), name="list-services"),
    path('<int:pk>/', service_detail, name="view-service"),
    path("service/get-quote/<int:pk>", get_quote, name="get_quote"),
    
    path("bookings/", view_bookings, name="list-bookings"),
    path("bookings/<int:pk>/", BookingDetail.as_view(), name="view-booking")
]
