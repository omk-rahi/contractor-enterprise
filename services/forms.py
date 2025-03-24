
from django import forms
from accounts.models import CustomUser
from .models import Quote, Booking, ServiceCost


class QuoteForm(forms.ModelForm):
    problems = forms.ModelMultipleChoiceField(
        queryset=ServiceCost.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Quote
        fields = ["problems", "description"]

    def __init__(self, *args, **kwargs):
        service = kwargs.pop('service', None)
        super().__init__(*args, **kwargs)
        if service:
            self.fields['problems'].queryset = ServiceCost.objects.filter(service=service)


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



