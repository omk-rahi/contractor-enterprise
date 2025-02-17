from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm

from .models import CustomUser, OTP, Address

class RegisterForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    phone = forms.CharField(min_length=10)

    class Meta:
        model = CustomUser
        fields = ['fullname', 'email', 'phone', 'password1', 'password2']

        
class StaffRegisterForm(RegisterForm):
    role = forms.CharField(initial="staff", disabled=True)

    class Meta:
        model = CustomUser
        fields = ['fullname', 'email', 'phone', 'password1', 'password2', "role"]

class VerifyForm(forms.ModelForm):
    class Meta:
        model = OTP
        fields = ['code']


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"autofocus": False}), label="Old Password")
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="New password confirmation")
    
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="New password confirmation")


class AddressForm(forms.ModelForm):
    pincode = forms.CharField(min_length=6, max_length=6)
    class Meta:
        model = Address
        fields = ["address_line", "pincode", "city", "state"]


class UserSettingForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ["fullname", "email", "phone", "profile_image"]