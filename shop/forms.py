from django import forms

from accounts.models import CustomUser
from .models import ProductSpec, Specification, WarrantyClaim

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


class WarrantyClaimForm(forms.ModelForm):
    class Meta:
        model = WarrantyClaim
        fields = ["order_item", "claim_reason"]
        labels = { 
            "order_item": "",
            "claim_reason": "",
        }
        widgets = {
            "order_item": forms.Select(attrs={"class": "form-control", "placeholder": "Select Product"}),
            "claim_reason": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Enter your claim reason"}),
        }