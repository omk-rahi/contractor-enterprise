from django.urls import path

from my_admin.views.quotes_views import *


quote_patterns = [
    path("", ListServiceQuoteView.as_view(), name="admin/list-quote"),
    path("<int:pk>/", DetailQuoteView.as_view(), name="quote-detail"),
    path("update/<int:pk>/", UpdateQuote, name="admin/update-quote"),    
]