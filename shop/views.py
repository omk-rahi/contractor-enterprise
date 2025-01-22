from django.shortcuts import render, redirect

# Create your views here.

def index(request):

    if request.user.is_superuser:
        return redirect("/admin")

    return render(request, 'shop/homepage.html')