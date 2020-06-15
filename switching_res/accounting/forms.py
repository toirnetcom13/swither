from django import forms
from .models import CommutationJournal, CircuitBreakers, NameOfSubstation

class JurForm(forms.ModelForm):
    class Meta:
        model = CommutationJournal
        fields = ['dispatcher_name', 'date_of_commutation', 'current_of_commutation', 'user_name', 'name_of_substation', 'branch']
        widjets = {
            'dispatcher_name': forms.Select(attrs={'class': 'form-control'}),
            'date_of_commutation': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'current_of_commutation': forms.NumberInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'name_of_substation': forms.Select(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
        }
