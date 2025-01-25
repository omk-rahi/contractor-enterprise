from django.views.generic import  View
from django.shortcuts import render
from shop.models import Payment

class ListPaymentView(View):
    def get(self, request):

        object_list = Payment.objects.filter()
        

        extra = {
            "title": "Payments",
            "fields" : ["id", "status", "date", "payment_method", "total"],
            "disable_action": True,
            "disable_create": True,
        }

        return render(request, "my_admin/list-template.html", context={"object_list": object_list, "extra" : extra}) 