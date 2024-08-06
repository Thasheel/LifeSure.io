from django import forms

from rootapp.models import LifeInsurance


class InsuranceForm(forms.ModelForm):
    class Meta:
        model=LifeInsurance
        fields=('__all__')
