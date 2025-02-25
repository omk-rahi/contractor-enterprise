
from django import forms
from accounts.models import CustomUser
from .models import Quote, Booking, ServiceCost


class NewQuoteForm(forms.ModelForm):

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40})
    )
    def __init__(self, *args, service=None, **kwargs):
        super(NewQuoteForm, self).__init__(*args, **kwargs)
        self.fields['problem'].queryset = ServiceCost.objects.filter(service=service)

    class Meta:
        model = Quote
        fields = ['problem', 'description']

class UpdateQuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = ['status', 'estimated_cost']


class UpdateBookingForm(forms.ModelForm):

    scheduled_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['staff'].queryset = CustomUser.objects.filter(role="staff")

    class Meta:
        model = Booking
        fields = ['staff', "additional_note", 'cost', 'status', 'scheduled_date']