from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, VerifyForm
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import generate_and_save_otp, verify_otp

from .models import CustomUser, Address
from .forms import AddressForm, UserSettingForm, CustomPasswordChangeForm

# Create your views here.

def index(request):
    return redirect('./login')



def register(request):

    if request.POST:
        form = RegisterForm(request.POST)


        if form.is_valid():
            user = form.save()
            Address.objects.create(user=user)
            return redirect("login")
    
    else :
        form = RegisterForm()

    
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



@login_required
def user_settings(request):

    address = get_object_or_404(Address, user=request.user)

    context = {
        "address_form": AddressForm(instance=address),
        "user_form": UserSettingForm(instance=request.user),
        "password_change_form": CustomPasswordChangeForm(request.user)
    }

    return render(request, "registration/user-settings.html", context)
    
@login_required
def save_address(request):
    if not request.POST:
        return redirect('user-settings')
    
    address = get_object_or_404(Address, user=request.user)

    address_form = AddressForm(request.POST, instance=address)

    if address_form.is_valid():
        address_form.save()
        messages.success(request, "Address Updated Successfully!")
        return redirect('user-settings')
    
    
@login_required
def save_profile(request):
    if not request.POST:
        return redirect('user-settings')
    
    profile = UserSettingForm(request.POST, request.FILES, instance=request.user)

    if profile.is_valid():
        profile.save()
        messages.success(request, "Profile Updated Successfully!")
        return redirect('user-settings')
