from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from reservas.models import Voo
from datetime import datetime, timedelta


class VooForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ['numero_voo', 'origem', 'destino', 'data_partida', 'data_chegada', 'nome', 'classe']


        widgets = {
            'numero_do_voo': forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Numero do Voo', 'class': 'form-control', 'autofocus': ''})),
            'origem': forms.TextInput(attrs={'class':'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'data_partida':forms.DateInput(attrs={'class':'form-control'}),
            'data_chegada': forms.DateInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'classe': forms.Select(attrs={'class': 'form-control'}, choices=[('Economica', 'Econômica'), ('Executiva', 'Executiva')])
        }


    def clean_data_chegada(self):
        data_chegada = self.cleaned_data['data_chegada']
        data_minima = (timezone.now() + timezone.timedelta(days=2)).strftime('%d-%m-%Y')

        if data_chegada < data_minima:
            raise ValidationError('A data de chegada deve ser pelo menos dois dias após a data atual.')

        return data_chegada