from django import forms
from .models import Compound

compounds = []
for item in Compound.objects.all():
    compounds.append((str(item), str(item)))


class ParametersForms(forms.Form):
    percentage = forms.IntegerField(
        required=True,
        label='Add compounds to your mixture (%):',
        min_value=0,
        max_value=100,
        widget= forms.NumberInput(attrs={'placeholder': 0})
    )
    compound = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select,
        choices=compounds,
        label='',
    )