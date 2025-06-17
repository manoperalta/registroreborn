from django import forms
from .models import CertidaoNascimento

class CertidaoNascimentoForm(forms.ModelForm):
    class Meta:
        model = CertidaoNascimento
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'hora_nascimento': forms.TimeInput(attrs={'type': 'time'}),
            'data_registro': forms.DateInput(attrs={'type': 'date'}),
        }
