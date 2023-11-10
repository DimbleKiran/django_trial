from .models import Customer, CustomerDetails
from django import forms


class CustomerForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class CustomerFormsPhoto(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['photo']


class CustomerDetailsForms(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = "__all__"

