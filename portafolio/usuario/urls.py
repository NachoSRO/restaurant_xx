from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from portafolio.usuario.views import *

urlpatterns = [
    #Usuarios
    path('inicio_usuarios/', InicioUsuarios.as_view(), name='inicio_usuarios'),
    path('listado_usuarios/', ListadoUsuario.as_view(),{'parametro_extra': 'Hola!'},name='listar_usuarios'),
    path('registrar_usuario/',RegistrarUsuario.as_view(),name = 'registrar_usuario'),
    path('actualizar_usuario/<int:pk>/',EditarUsuario.as_view(), name = 'actualizar_usuario'),
    path('eliminar_usuario/<int:pk>/',EliminarUsuario.as_view(), name='eliminar_usuario'),

    #Grupos
    path('inicio_grupos/', InicioGrupos.as_view(), name='inicio_grupos'),
    path('listado_grupos/', ListadoGrupo.as_view(),name='listado_grupos'),
    path('eliminar_grupos/<int:pk>/',EliminarGrupo.as_view(), name='eliminar_grupos'),

    #Roles
    path('inicio_rol/', InicioRols.as_view(), name='inicio_rol'),
    path('listado_roles/', ListadoRol.as_view(),name='listar_rol'),
    path('registrar_rol/',RegistrarRol.as_view(),name = 'registrar_rol'),
    path('actualizar_rol/<int:pk>/',EditarRol.as_view(), name = 'actualizar_rol'),
    path('eliminar_rol/<int:pk>/',EliminarRol.as_view(), name='eliminar_rol'),
]
