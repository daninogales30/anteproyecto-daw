from django import forms
from .models import Entrada


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la entrada'}),
            'body': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Escribe el contenido aquí...', 'rows': 6}),
        }
