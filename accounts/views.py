from django.shortcuts import render, redirect
from .forms import RegisterForm, VerifyForm
from django.core.mail import send_mail
from django.contrib import messages

from .utils import generate_and_save_otp, verify_otp

from .models import CustomUser

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

    print(request.path.split('/'))
    
    return render(request, "registration/register.html", {"form": form})


def verify(request):

    if request.POST:
        form = VerifyForm(request.POST)


        if form.is_valid() and verify_otp(request.user.id, request.POST['code']):
            
            user = CustomUser.objects.get(pk=request.user.id)

            user.is_verified = True
            user.save()

            return redirect("home")

        else:
            form.add_error("code", "Invalid code")
        
    else: 
        form = VerifyForm()

    return render(request, "registration/verify.html", {"form": form})


def send_otp(request):
    otp = generate_and_save_otp(user=request.user)


    send_mail(
                subject='Verify Your Email Address',
                message=f"Hello {request.user.fullname},\n\nYour OTP code is {otp.code}. It is valid for 5 minutes.\n\nBest regards,\nContractor Enterprise",
                from_email="admin@gmail.com",
                recipient_list=[request.user.email],
                fail_silently=False,
            )

    messages.add_message(request, messages.SUCCESS, message="OTP sent to your email.")

    return redirect("verify")