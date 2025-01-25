from django.views.generic import View
from django.shortcuts import render
from accounts.models import CustomUser

# Create your views here.

class ListCustomerView(View):
    def get(self, request):

        object_list = CustomUser.objects.filter(role='customer')
        
        extra = {
            "title": "Customers",
            "fields" : ["id", "fullname", "email", "phone"],
            "disable_action": True,
            "disable_create": True,
        }

        return render(request, "my_admin/list-template.html", context={"object_list": object_list, "extra" : extra}) 