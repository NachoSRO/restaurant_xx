from django.urls import path
from portafolio.receta.views import *

urlpatterns = [
    
    #Receta
    path('listado_recetas/', ListadoReceta.as_view(), name='listado_recetas'),
    path('crear_recetas/', RegistrarReta.as_view(), name='crear_recetas'),
    path('modificar_recetas/<pk>/', ModificarReceta.as_view(), name='modificar_recetas'),
    path('eliminar_receta/<pk>/',EliminarReceta.as_view(),name="eliminar_receta"),

]