from django.urls import path
from django.views.generic import TemplateView
from portafolio.cliente.views import *

urlpatterns = [
     #CLIENTE
     path('inicio_clientes/', InicioCliente.as_view(), name='inicio_clientes'),
     path('listado_clientes/', ListadoCliente.as_view(),name='listar_clientes'),
     path('registrar_clientes/',RegistrarCliente.as_view(),name = 'registrar_clientes'),
     path('actualizar_clientes/<int:pk>/',EditarCliente.as_view(), name = 'actualizar_clientes'),
     path('eliminar_clientes/<int:pk>/',EliminarCliente.as_view(), name='eliminar_clientes'),

     #MESA
     path('inicio_mesas/', InicioMesas.as_view(), name='inicio_mesas'),
     path('listado_mesas/', ListadoMesa.as_view(),name='listar_mesas'),
     path('registrar_mesas/',RegistrarMesa.as_view(),name = 'registrar_mesas'),
     path('actualizar_mesas/<int:pk>/',EditarMesa.as_view(), name = 'actualizar_mesas'),
     path('eliminar_mesas/<int:pk>/',EliminarMesa.as_view(), name='eliminar_mesas'),

]
