from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.views import LoginView

# Create your views here.

def index(request):
    return redirect('./login')


def register(request):

    if request.POST:
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    
    else :
        form = RegisterForm()
    
    return render(request, "registration/register.html", {"form": form})

