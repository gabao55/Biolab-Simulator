from django import forms
from .models import Compound

#TODO: Remove this file, because it's not being used
compounds = []
for compound in Compound.objects.all():
    compounds.append((str(compound.name), str(compound.name)))

esther_types = []
for esther_type in Compound.objects.all():
    esther_types.append((str(esther_type.esther_type), str(esther_type.esther_type)))


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
    esther_type = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select,
        choices=esther_types,
        label='',
    )