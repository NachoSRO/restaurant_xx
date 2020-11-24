from django.urls import path
from portafolio.reportes.views import *

urlpatterns = [
    
    #Reporte productos
    # path('inicio_reportes/', InicioReportes.as_view(), name='inicio_reportes'),
    path('listado_reportes/', reportes,name='listado_reportes'),

]