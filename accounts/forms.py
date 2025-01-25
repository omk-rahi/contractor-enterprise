from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, OTP

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

    