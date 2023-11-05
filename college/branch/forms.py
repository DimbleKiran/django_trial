from django import forms
from .models import Mechanical


class MechForms(forms.ModelForm):
    class Meta:
        model = Mechanical
        fields = "__all__"

    def clean_age(self):
        your_age = self.cleaned_data['age']
        if your_age >= 16:
            return your_age
        else:
            raise forms.ValidationError('Barkya Ghari ja')
