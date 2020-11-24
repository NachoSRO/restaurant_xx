from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from portafolio.producto.models import *
from portafolio.usuario.models import *
from portafolio.cliente.models import *
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from portafolio.usuario.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
# Create your views here.

@login_required
def reportes(request):
    productos = Producto.objects.all()
    usuarios = Usuario.objects.all()
    clientes = Cliente.objects.all()
    proveedores = Proveedor.objects.all()
    mesas = Mesa.objects.all()
    data = {
           'productos': productos,
           'usuarios' : usuarios,
           'clientes' : clientes,
           'proveedores' : proveedores,
           'mesas' : mesas
           }
    return render(request, 'reportes/report_producto.html',data)