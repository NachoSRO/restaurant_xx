from django import forms
from portafolio.producto.models import *
from django.forms.models import inlineformset_factory


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('cod_producto','name','tipo','precio_Compra','stock','gramaje','descripcion')
        widgets = {
            'cod_producto': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Codigo producto',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre producto',
                }
            ),
            'tipo': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'tipo',
                }                
            ),
            'precio_Compra': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Precio de compra',
                }
            ),
            'stock': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'stock del producto',
                }
            ),
            'gramaje': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'gramaje',
                }                
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Descripcion',
                }                
            ),
        }

    def clean_cod_producto(self):
        return self.cleaned_data['cod_producto'].title()
    
    def clean_name(self):
        return self.cleaned_data['name'].title()

class FormularioProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('rut','nombre','telefono','direccion')
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Rut Proveedor',
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre Proveedor',
                }                
            ),
            'telefono': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '9XXXXXXXX',
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'direccion',
                }
            ),           
        }

class FormularioIngresoPedidoProd(forms.ModelForm):
    class Meta:
        model = IngresoPedidoProd
        fields = ('codigo','fecha_ingreso','proveedor')
        widgets = {
            'codigo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Codigo Ingreso pedido',
                }
            ),
            'fecha_ingreso': forms.DateTimeInput(
                attrs = {
                    'class': 'form-control',
                }                
            ),
            'proveedor': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),        
        }

class FormularioFacturaPedidoProd(forms.ModelForm):
    class Meta:
        model = FacturaPedidoProd
        fields = ('ingreso_producto','producto','cantidad')
        widgets = {
            'ingreso_producto': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'producto': forms.Select(
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
# Ingreso se nuestro inline formset
IngresoProductoFormSet = inlineformset_factory(
    IngresoPedidoProd, FacturaPedidoProd, form = FormularioFacturaPedidoProd,
    extra = 5, can_delete=True
)

class FormularioSolicitudProducto(forms.ModelForm):
    class Meta:
        model = SolicitudProducto
        fields = ('codigo','fecha_solicitud')
        widgets = {
            'codigo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Codigo Ingreso pedido',
                }
            ),
            'fecha_solicitud': forms.DateTimeInput(
                attrs = {
                    'class': 'form-control',
                }                
            )     
        }

class FormularioDetalleSolicitud(forms.ModelForm):
    class Meta:
        model = DetalleSolicitudProd
        fields = ('solicitud_producto','producto','cantidad')
        widgets = {
            'solicitud_producto': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'producto': forms.Select(
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

SolicitudProductoFormSet = inlineformset_factory(
    SolicitudProducto, DetalleSolicitudProd, form = FormularioDetalleSolicitud,
    extra = 5, can_delete=True
)