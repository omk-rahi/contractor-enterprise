from django import forms

from accounts.models import CustomUser
from .models import ProductSpec, Specification

class UpdateProductSpecForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specification'].queryset = Specification.objects.filter(category=(kwargs['instance'].product.category))
        self.fields['product'].disabled = True


    class Meta:
        model = ProductSpec
        fields = '__all__'


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ["fullname", "email", "phone"]