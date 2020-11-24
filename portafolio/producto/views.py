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
from portafolio.producto.models import *
from portafolio.producto.forms import *
from portafolio.producto.admin import *
from portafolio.usuario.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin
from django.db import transaction 

# Create your views here.

############### PRODUCTOS ###################
class InicioProductos(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name='productos/listar_producto.html'
    permission_required = ('producto.view_producto', 'producto.add_producto',
                           'producto.delete_producto', 'producto.change_producto')

class ListadoProducto(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = Producto
    permission_required = ('producto.view_producto', 'producto.add_producto',
                           'producto.delete_producto', 'producto.change_producto')

    def get_queryset(self):
        return self.model.objects.all()
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('productos:inicio_productos')

class RegistrarProducto(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    model = Producto
    form_class = FormularioProducto
    template_name = 'productos/crear_producto.html'
    permission_required = ('producto.view_producto', 'producto.add_producto',
                           'producto.delete_producto', 'producto.change_producto')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_producto = Producto(
                    cod_producto=form.cleaned_data.get('cod_producto'),
                    name=form.cleaned_data.get('name'),
                    tipo=form.cleaned_data.get('tipo'),
                    precio_Compra=form.cleaned_data.get('precio_Compra'),
                    stock=form.cleaned_data.get('stock'),
                    gramaje=form.cleaned_data.get('gramaje'),
                    descripcion=form.cleaned_data.get('descripcion')
                )
                nuevo_producto.save()
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
            return redirect('productos:inicio_productos')

class EditarProducto(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = Producto
    form_class = FormularioProducto
    template_name = 'productos/editar_producto.html'
    permission_required = ('producto.view_producto', 'producto.add_producto',
                           'producto.delete_producto', 'producto.change_producto')

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
            return redirect('productos:inicio_productos')

class EliminarProducto(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    model = Producto
    form_class = FormularioProducto
    template_name = 'productos/eliminar_producto.html'
    permission_required = ('producto.view_producto', 'producto.add_producto',
                           'producto.delete_producto', 'producto.change_producto')

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
            return redirect('productos:inicio_productos')


################ PROVEEDOR ####################
class InicioProveedor(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name='productos/listar_proveedor.html'
    permission_required = ('producto.view_proveedor', 'producto.add_proveedor',
                           'producto.delete_proveedor', 'producto.change_proveedor')

class ListadoProveedores(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = Proveedor
    permission_required = ('producto.view_proveedor', 'producto.add_proveedor',
                           'producto.delete_proveedor', 'producto.change_proveedor')

    def get_queryset(self):
        return self.model.objects.all()
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('productos:inicio_proveedores')

class RegistrarProveedor(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    model = Proveedor
    form_class = FormularioProveedor
    template_name = 'productos/crear_proveedor.html'
    permission_required = ('producto.view_proveedor', 'producto.add_proveedor',
                           'producto.delete_proveedor', 'producto.change_proveedor')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_proveedor = Proveedor(
                    rut=form.cleaned_data.get('rut'),
                    nombre=form.cleaned_data.get('nombre'),
                    telefono=form.cleaned_data.get('telefono'),
                    direccion=form.cleaned_data.get('direccion')
                )
                nuevo_proveedor.save()
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
            return redirect('productos:inicio_proveedores')

class EditarProveedor(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = Proveedor
    form_class = FormularioProveedor
    template_name = 'productos/editar_proveedor.html'
    permission_required = ('producto.view_proveedor', 'producto.add_proveedor',
                           'producto.delete_proveedor', 'producto.change_proveedor')

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
            return redirect('productos:inicio_proveedores')

class EliminarProveedor(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    model = Proveedor
    form_class = FormularioProveedor
    template_name = 'productos/eliminar_proveedor.html'
    permission_required = ('producto.view_proveedor', 'producto.add_proveedor',
                           'producto.delete_proveedor', 'producto.change_proveedor')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            proveedor = self.get_object()
            proveedor.delete()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            #return redirect('productos:inicio_proveedores')
            mensaje = f'{self.model.__name__} no se ha podido actualizar!'
            error = form.errors
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 400
            return response


########## INGRESO DE FACTURA PEDIDOS #########################
class InicioIngresoPedido(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name='productos/listar_pedidos.html'
    permission_required = ('producto.view_facturapedidoprod', 'producto.add_facturapedidoprod',
                           'producto.delete_facturapedidoprod', 'producto.change_facturapedidoprod',
                           'producto.view_ingresopedidoprod', 'producto.add_ingresopedidoprod',
                           'producto.delete_ingresopedidoprod', 'producto.change_ingresopedidoprod')

class ListadoRegistroPedidos(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = IngresoPedidoProd
    permission_required = ('producto.view_facturapedidoprod', 'producto.add_facturapedidoprod',
                           'producto.delete_facturapedidoprod', 'producto.change_facturapedidoprod',
                           'producto.view_ingresopedidoprod', 'producto.add_ingresopedidoprod',
                           'producto.delete_ingresopedidoprod', 'producto.change_ingresopedidoprod')

    def get_queryset(self):
        return self.model.objects.all()
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('productos:inicio_pedidos')

class RegistrarPedidoProd(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    model = IngresoPedidoProd
    form_class = FormularioIngresoPedidoProd
    template_name = 'productos/crear_pedidos.html'
    permission_required = ('producto.view_facturapedidoprod', 'producto.add_facturapedidoprod',
                           'producto.delete_facturapedidoprod', 'producto.change_facturapedidoprod',
                           'producto.view_ingresopedidoprod', 'producto.add_ingresopedidoprod',
                           'producto.delete_ingresopedidoprod', 'producto.change_ingresopedidoprod')

    def get_context_data(self, **kwargs):
        data = super(RegistrarPedidoProd, self).get_context_data(**kwargs)
        if self.request.POST:
            data['pedido'] = IngresoProductoFormSet(self.request.POST)
        else:
            data['pedido'] = IngresoProductoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['pedido']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
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
        return super(RegistrarPedidoProd,self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('productos:inicio_pedidos')

class EditarPedido(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = IngresoPedidoProd
    # form_class = FormularioIngresoPedidoProd
    template_name = 'productos/editar_pedidos.html'
    permission_required = ('producto.view_facturapedidoprod', 'producto.add_facturapedidoprod',
                           'producto.delete_facturapedidoprod', 'producto.change_facturapedidoprod',
                           'producto.view_ingresopedidoprod', 'producto.add_ingresopedidoprod',
                           'producto.delete_ingresopedidoprod', 'producto.change_ingresopedidoprod')
    # success_url=reverse_lazy('producto:inicio_pedidos')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(EditarPedido, self).get_context_data(**kwargs)
        if self.request.POST:
            context['pedido'] = IngresoProductoFormSet(self.request.POST, instance=self.object)
            context['pedido'].full_clean()
        else:
            context['pedido'] = IngresoProductoFormSet(instance=self.object)
        return context

    def form_valid(self, form):
            context = self.get_context_data()
            formset = context['pedido']
            with transaction.atomic():
                self.object = form.save()
                if formset.is_valid():
                    response = super().form_valid(form)
                    formset.instance = self.object
                    formset.save()
                    return response
            return super(EditarPedido,self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('productos:inicio_pedidos')

class EliminarPedido(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    model = IngresoPedidoProd
    form_class = IngresoProductoFormSet
    template_name = 'productos/eliminar_pedido.html'
    permission_required = ('producto.view_facturapedidoprod', 'producto.add_facturapedidoprod',
                           'producto.delete_facturapedidoprod', 'producto.change_facturapedidoprod',
                           'producto.view_ingresopedidoprod', 'producto.add_ingresopedidoprod',
                           'producto.delete_ingresopedidoprod', 'producto.change_ingresopedidoprod')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            proveedor = self.get_object()
            proveedor.delete()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            #return redirect('productos:inicio_proveedores')
            mensaje = f'{self.model.__name__} no se ha podido actualizar!'
            error = form.errors
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 400
            return response

######### SOLICITUD DE PRODUCTOS ###############
class InicioSolicitudPedido(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name='productos/listar_solicitudes.html'
    permission_required = ('producto.view_solicitudproducto', 'producto.add_solicitudproducto',
                           'producto.view_detallesolicitudprod', 'producto.add_detallesolicitudprod')

class ListadoSolicitudPedidos(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = SolicitudProducto
    permission_required = ('producto.view_solicitudproducto', 'producto.add_solicitudproducto',
                           'producto.view_detallesolicitudprod', 'producto.add_detallesolicitudprod')

    def get_queryset(self):
        return self.model.objects.all()
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('productos:inicio_solicitudes')

class RegistrarSolicitud(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    model = SolicitudProducto
    form_class = FormularioSolicitudProducto
    template_name = 'productos/crear_solicitudes.html'
    permission_required = ('producto.view_solicitudproducto', 'producto.add_solicitudproducto',
                           'producto.view_detallesolicitudprod', 'producto.add_detallesolicitudprod')

    def get_context_data(self, **kwargs):
        data = super(RegistrarSolicitud, self).get_context_data(**kwargs)
        if self.request.POST:
            data['pedido'] = SolicitudProductoFormSet(self.request.POST)
        else:
            data['pedido'] = SolicitudProductoFormSet()
        return data

    def form_valid(self,form):
        context = self.get_context_data()
        pedido = context['pedido']
        with transaction.atomic():
            self.object = form.save()

            if pedido.is_valid():
                pedido.instance = self.object
                pedido.save()
        return super(RegistrarSolicitud,self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('productos:inicio_solicitudes')

class EditarSolicitudes(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = SolicitudProducto
    # form_class = FormularioIngresoPedidoProd
    template_name = 'productos/editar_solicitudes.html'
    permission_required = (
                           'producto.delete_solicitudproducto', 'producto.change_solicitudproducto',
                           'producto.delete_detallesolicitudprod', 'producto.change_detallesolicitudprod')
    # success_url=reverse_lazy('producto:inicio_pedidos')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(EditarSolicitudes, self).get_context_data(**kwargs)
        if self.request.POST:
            context['pedido'] = SolicitudProductoFormSet(self.request.POST, instance=self.object)
            context['pedido'].full_clean()
        else:
            context['pedido'] = SolicitudProductoFormSet(instance=self.object)
        return context

    def form_valid(self, form):
            context = self.get_context_data()
            formset = context['pedido']
            with transaction.atomic():
                self.object = form.save()
                if formset.is_valid():
                    response = super().form_valid(form)
                    formset.instance = self.object
                    formset.save()
                    return response
            return super(EditarSolicitudes,self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('productos:inicio_solicitudes')

class EliminarSolicitudes(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    model = SolicitudProducto
    form_class = SolicitudProductoFormSet
    template_name = 'productos/eliminar_solicitudes.html'
    permission_required = (
                           'producto.delete_solicitudproducto', 'producto.change_solicitudproducto',
                           'producto.delete_detallesolicitudprod', 'producto.change_detallesolicitudprod')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            proveedor = self.get_object()
            proveedor.delete()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            #return redirect('productos:inicio_proveedores')
            mensaje = f'{self.model.__name__} no se ha podido actualizar!'
            error = form.errors
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 400
            return response