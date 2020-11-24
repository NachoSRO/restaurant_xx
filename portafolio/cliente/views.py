import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from portafolio.cliente.models import *
from portafolio.cliente.forms import *
from portafolio.usuario.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin

# Create your views here.

############### PRODUCTOS ###################
class InicioCliente(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name='clientes/listar_cliente.html'
    permission_required = ('cliente.view_cliente', 'cliente.add_cliente',
                           'cliente.delete_cliente', 'cliente.change_cliente')

class ListadoCliente(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = Cliente
    permission_required = ('cliente.view_cliente', 'cliente.add_cliente',
                           'cliente.delete_cliente', 'cliente.change_cliente')

    def get_queryset(self):
        return self.model.objects.all()
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('clientes:inicio_clientes')

class RegistrarCliente(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    model = Cliente
    form_class = FormularioCliente
    template_name = 'clientes/crear_cliente.html'
    permission_required = ('cliente.view_cliente', 'cliente.add_cliente',
                           'cliente.delete_cliente', 'cliente.change_cliente')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_cliente = Cliente(
                    rut=form.cleaned_data.get('rut'),
                    nombre=form.cleaned_data.get('nombre'),
                    telefono=form.cleaned_data.get('telefono'),
                )
                nuevo_cliente.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('clientes:inicio_clientes')

class EditarCliente(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = Cliente
    form_class = FormularioCliente
    template_name = 'clientes/editar_cliente.html'
    permission_required = ('cliente.view_cliente', 'cliente.add_cliente',
                           'cliente.delete_cliente', 'cliente.change_cliente')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('clientes:inicio_clientes')

class EliminarCliente(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    model = Cliente
    form_class = FormularioCliente
    template_name = 'clientes/eliminar_cliente.html'
    permission_required = ('cliente.view_cliente', 'cliente.add_cliente',
                           'cliente.delete_cliente', 'cliente.change_cliente')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            producto = self.get_object()
            producto.delete()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('clientes:inicio_clientes')

############### MESAS ###################
class InicioMesas(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name='clientes/listar_mesa.html'
    permission_required = ('cliente.view_mesa', 'cliente.add_mesa',
                           'cliente.delete_mesa', 'cliente.change_mesa')

class ListadoMesa(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = Mesa
    permission_required = ('cliente.view_mesa', 'cliente.add_mesa',
                           'cliente.delete_mesa', 'cliente.change_mesa')

    def get_queryset(self):
        return self.model.objects.all()
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('clientes:inicio_mesas')

class RegistrarMesa(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    model = Mesa
    form_class = FormularioMesa
    template_name = 'clientes/crear_mesa.html'
    permission_required = ('cliente.view_mesa', 'cliente.add_mesa',
                           'cliente.delete_mesa', 'cliente.change_mesa')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nueva_mesa = Mesa(
                    num_persona=form.cleaned_data.get('num_persona'),
                    estado=form.cleaned_data.get('estado'),
                )
                nueva_mesa.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('clientes:inicio_mesas')

class EditarMesa(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = Mesa
    form_class = FormularioMesa
    template_name = 'clientes/editar_mesa.html'
    permission_required = ('cliente.view_mesa', 'cliente.add_mesa',
                           'cliente.delete_mesa', 'cliente.change_mesa')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('clientes:inicio_mesas')

class EliminarMesa(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    model = Mesa
    form_class = FormularioMesa
    template_name = 'clientes/eliminar_mesa.html'
    permission_required = ('cliente.view_mesa', 'cliente.add_mesa',
                           'cliente.delete_mesa', 'cliente.change_mesa')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            producto = self.get_object()
            producto.delete()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('clientes:inicio_mesas')