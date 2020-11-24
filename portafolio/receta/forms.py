from django import forms
from portafolio.receta.models import *
from django.forms.models import inlineformset_factory

class FormularioReceta(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('nombre','descripcion','tipo','precio')
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre receta',
                }                
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'tipo': forms.Select(
                attrs = {
                    'class': 'form-control',
                }                
            ),
            'precio': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                }
            ), 
        }

class FormularioDetalleReceta(forms.ModelForm):
    class Meta:
        model = DetalleReceta
        fields = ('receta_id','producto_id','cantidad')
        widgets = {
            'receta_id': forms.Select(
                attrs = {
                    'class': 'form-control',
                }                
            ),
            'producto_id': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'cantidad': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                }
            ),           
        }

RecetaFormSet = inlineformset_factory(
    Receta, DetalleReceta, form = FormularioDetalleReceta,
    extra = 7, can_delete=True
)