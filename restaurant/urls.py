"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path,include,re_path
from django.contrib.auth.decorators import login_required
from portafolio.usuario.views import *
from portafolio.producto.views import *
from portafolio.reportes.views import *
from portafolio.cliente.views import *
from portafolio.receta.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',include(('portafolio.usuario.urls','usuarios'))),
    path('productos/',include(('portafolio.producto.urls','productos'))),
    path('reportes/',include(('portafolio.reportes.urls','reportes'))),
    path('clientes/',include(('portafolio.cliente.urls','clientes'))),
    path('recetas/',include(('portafolio.receta.urls','recetas'))),
    #path('k/',include('portafolio.urls')),
    path('',Inicio.as_view(), name = 'index'),
    path('accounts/login/',Login.as_view(),name="Login"),
    path('logout/',login_required(logoutUsuario),name="logout"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)