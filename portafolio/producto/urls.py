from django.urls import path
from django.views.generic import TemplateView
from portafolio.producto.views import *

urlpatterns = [
     #Productos
     path('inicio_productos/', InicioProductos.as_view(), name='inicio_productos'),
     path('listado_productos/', ListadoProducto.as_view(),name='listar_productos'),
     path('registrar_productos/',RegistrarProducto.as_view(),name = 'registrar_productos'),
     path('actualizar_productos/<int:pk>/',EditarProducto.as_view(), name = 'actualizar_productos'),
     path('eliminar_productos/<int:pk>/',EliminarProducto.as_view(), name='eliminar_productos'),

     # #Proveedores
     path('inicio_proveedores/', InicioProveedor.as_view(), name='inicio_proveedores'),
     path('listado_proveedores/', ListadoProveedores.as_view(),name='listar_proveedores'),
     path('registrar_proveedores/',RegistrarProveedor.as_view(),name = 'registrar_proveedores'),
     path('actualizar_proveedores/<int:pk>/',EditarProveedor.as_view(), name = 'actualizar_proveedores'),
     path('eliminar_proveedores/<int:pk>/',EliminarProveedor.as_view(), name='eliminar_proveedores'),

     #Ingreso facturas
     path('inicio_pedidos/', InicioIngresoPedido.as_view(), name='inicio_pedidos'),
     path('listado_registro_pedidos/',ListadoRegistroPedidos.as_view(),name='listado_registro_pedidos'),
     path('registrar_pedido/', RegistrarPedidoProd.as_view(), name='registrar_pedido'),
     path('actualizar_pedido/<int:pk>/',EditarPedido.as_view(), name = 'actualizar_pedido'),
     path('eliminar_pedido/<int:pk>/',EliminarPedido.as_view(), name='eliminar_pedido'),

     #Solicitud de productos
     path('inicio_solicitudes/', InicioSolicitudPedido.as_view(), name='inicio_solicitudes'),
     path('listar_solicitudes/',ListadoSolicitudPedidos.as_view(),name='listar_solicitudes'),
     path('registrar_solicitudes/', RegistrarSolicitud.as_view(), name='registrar_solicitudes'),
     path('actualizar_solicitudes/<int:pk>/',EditarSolicitudes.as_view(), name = 'actualizar_solicitudes'),
     path('eliminar_solicitudes/<int:pk>/',EliminarSolicitudes.as_view(), name='eliminar_solicitudes'),
]
