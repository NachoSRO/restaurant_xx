from django.contrib import admin
from functools import partial
from django import forms
from simple_history.admin import SimpleHistoryAdmin
from portafolio.producto.models import *

# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
     fields = ['rut','nombre']
     list_display = ['rut','nombre']

class FacturaPedidoProdInline(admin.StackedInline):
    model = FacturaPedidoProd


class IngresoProdAdmin(admin.ModelAdmin):
    # Registramos el inline en la persona
    inlines = [FacturaPedidoProdInline]

class DetalleSolicitudInline(admin.StackedInline):
    model = DetalleSolicitudProd

class SolicitudProdAdmin(admin.ModelAdmin):
    inlines = [DetalleSolicitudInline]

admin.site.register(Producto)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(IngresoPedidoProd,IngresoProdAdmin)
admin.site.register(SolicitudProducto,SolicitudProdAdmin)

