import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from portafolio.usuario.models import *
from portafolio.usuario.forms import *
from portafolio.usuario.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin
from django.contrib.auth.models import Group


class Inicio(LoginRequiredMixin,TemplateView):
    """Clase que renderiza el index del sistema"""

    template_name = 'index.html'


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class InicioUsuarios(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name='usuarios/listar_usuario.html'
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')


class ListadoUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = Usuario
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')

    def get_queryset(self): 
        return self.model.objects.all()

    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('usuarios:inicio_usuarios')


class RegistrarUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')

    def post(self, request, *args, **kwargs):
        nuevo_usuario = {}
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_usuario = Usuario(
                    email=form.cleaned_data.get('email'),
                    username=form.cleaned_data.get('username'),
                    nombres=form.cleaned_data.get('nombres'),
                    apellidos=form.cleaned_data.get('apellidos'),
                    rol=form.cleaned_data.get('rol'),
                    is_staff=form.cleaned_data.get('is_staff'),
                    is_active=form.cleaned_data.get('is_active')
                )
                nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                nuevo_usuario.save()
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
            return redirect('usuarios:inicio_usuarios')


class EditarUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/editar_usuario.html'
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')

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
            return redirect('usuarios:inicio_usuarios')


class EliminarUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar_usuario.html'
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            usuario = self.get_object()
            usuario.usuario_activo = False
            usuario.delete()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('usuarios:inicio_usuarios')



#Roles#####
class InicioRols(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name='usuarios/listar_rol.html'
    permission_required = ('usuario.view_rol', 'usuario.add_rol',
                           'usuario.delete_rol', 'usuario.change_rol')

class ListadoRol(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = Rol
    permission_required = ('usuario.view_rol', 'usuario.add_rol',
                           'usuario.delete_rol', 'usuario.change_rol')

    def get_queryset(self): 
        return self.model.objects.all()

    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('usuarios:inicio_rol')

class RegistrarRol(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    model = Rol
    form_class = FormularioRol
    template_name = 'usuarios/crear_rol.html'
    permission_required = ('usuario.view_rol', 'usuario.add_rol',
                           'usuario.delete_rol', 'usuario.change_rol')

    def post(self, request, *args, **kwargs):
        nuevo_rol = {}
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
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
            return redirect('usuarios:inicio_rol')

class EditarRol(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = Rol
    form_class = FormularioRol
    template_name = 'usuarios/editar_rol.html'
    permission_required = ('usuario.view_rol', 'usuario.add_rol',
                           'usuario.delete_rol', 'usuario.change_rol')

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
            return redirect('usuarios:inicio_rol') 
    
class EliminarRol(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    model = Rol
    template_name = 'usuarios/eliminar_rol.html'
    permission_required = ('usuario.view_rol', 'usuario.add_rol',
                           'usuario.delete_rol', 'usuario.change_rol')

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            usuario = self.get_object()
            usuario.delete()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('usuarios:inicio_rol')

class InicioGrupos(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name='usuarios/listar_grupo.html'
    permission_required = ('auth.view_group', 'auth.add_group',
                           'auth.delete_group', 'auth.change_group')

class ListadoGrupo(LoginYSuperStaffMixin, ValidarPermisosMixin,ListView):
    model = Group
    permission_required = ('auth.view_group', 'auth.add_group',
                           'auth.delete_group', 'auth.change_group')
    
    def get_queryset(self): 
        return self.model.objects.all()

    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('usuarios:inicio_grupos')

class EliminarGrupo(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    model = Group
    template_name = 'usuarios/eliminar_grupo.html'
    permission_required = ('auth.view_group', 'auth.add_group',
                           'auth.delete_group', 'auth.change_group')

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            usuario = self.get_object()
            usuario.delete()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('usuarios:inicio_grupos')