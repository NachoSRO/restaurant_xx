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
from portafolio.receta.models import *
from portafolio.receta.forms import *
from portafolio.receta.admin import *
from portafolio.usuario.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin
from django.db import transaction 
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory

# Create your views here.

class RegistrarRetaD(LoginRequiredMixin,ValidarPermisosMixin,CreateView):
    model = Receta
    fields = ['nombre','descripcion','precio']

class ListadoReceta(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = Receta
    template_name = 'recetas/listar_recetas.html'
    context_object_name = 'recetas'
    queryset = Receta.objects.all()
    permission_required = ('receta.view_receta', 'receta.add_receta',
                           'receta.delete_receta', 'receta.change_receta')

class RegistrarReta(LoginRequiredMixin,ValidarPermisosMixin,CreateView):
    model = Receta
    fields = ['nombre','descripcion','tipo','precio']
    template_name = 'recetas/crear_recetas.html'
    permission_required = ('receta.view_receta', 'receta.add_receta',
                           'receta.delete_receta', 'receta.change_receta')

    def get_context_data(self,**kwargs):
        data = super(RegistrarReta,self).get_context_data(**kwargs)
        if self.request.POST:
            data['recetaformset'] = RecetaFormSet(self.request.POST)
        else:
            data['recetaformset'] = RecetaFormSet()
        return data
    
    def form_valid(self,form):
        context = self.get_context_data()
        recetaformset = context['recetaformset']
        with transaction.atomic():
            self.object = form.save()

            if recetaformset.is_valid():
                recetaformset.instance = self.object
                recetaformset.save()
        return super(RegistrarReta,self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recetas:listado_recetas')
 
class ModificarReceta(LoginRequiredMixin,ValidarPermisosMixin,UpdateView):
    model = Receta
    template_name = 'recetas/modificar_receta.html'
    fields = ['nombre','descripcion','precio']
    permission_required = ('receta.view_receta', 'receta.add_receta',
                           'receta.delete_receta', 'receta.change_receta')

    def get_context_data(self,**kwargs):
        data = super(ModificarReceta,self).get_context_data(**kwargs)
        if self.request.POST:
            data['recetaformset'] = RecetaFormSet(self.request.POST,instance=self.object)
        else:
            data['recetaformset'] = RecetaFormSet(instance=self.object)
        return data

    def form_valid(self,form):
        context = self.get_context_data()
        recetaformset = context['recetaformset']
        with transaction.atomic():
            self.object = form.save()

            if recetaformset.is_valid():
                recetaformset.instance = self.object
                recetaformset.save()
        return super(ModificarReceta,self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recetas:listado_recetas')

class EliminarReceta(LoginRequiredMixin,ValidarPermisosMixin,DeleteView):
    model = Receta
    inlines = [DetalleRecetaInline]
    permission_required = ('receta.view_receta', 'receta.add_receta',
                           'receta.delete_receta', 'receta.change_receta')
    template_name = 'recetas/receta_confirm_delete.html'
    success_url = reverse_lazy('recetas:listado_recetas')

    # model = Receta
    # form_class = FormularioReceta
    # template_name = 'recetas/crear_recetas.html'
    # permission_required = 'receta.add_receta'

    # def get_context_data(self, **kwargs):
    #     data = super(RegistrarReta, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['receta'] = RecetaFormSet(self.request.POST)
    #     else:
    #         data['receta'] = RecetaFormSet()
    #     return data

    # def form_valid(self,form):
    #     context = self.get_context_data()
    #     formset = context['receta']
    #     with transaction.atomic():
    #         self.object = form.save()
    #         if formset.is_valid():
    #             formset.instance = self.object
    #             formset.save()
    #             mensaje = f'{self.model.__name__} registrado correctamente!'
    #             error = 'No hay error!'
    #             response = JsonResponse({'mensaje':mensaje,'error':error})
    #             response.status_code = 201
    #             return response
    #         else:
    #             mensaje = f'{self.model.__name__} no se ha podido registrar!'
    #             error = form.errors
    #             response = JsonResponse({'mensaje': mensaje, 'error': error})
    #             response.status_code = 400
    #             return response
    #     return super(RegistrarReta,self).form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy('recetas/listar_recetas.html')

    