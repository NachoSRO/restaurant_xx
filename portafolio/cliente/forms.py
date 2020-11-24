from django import forms
from portafolio.cliente.models import *

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('rut','nombre','telefono',)
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Rut Cliente',
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre Cliente',
                }                
            ),
            'telefono': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '9XXXXXXXX',
                }
            )         
        }

class FormularioMesa(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ('num_persona','estado',)
        widgets = {
            'num_persona': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'numero de personas',
                }
            ),
            'estado': forms.Select(
                attrs = {
                    'class': 'form-control',
                }                
            )     
        }