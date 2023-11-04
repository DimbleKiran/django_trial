from .models import Customer
from django import forms


class CustomerForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
