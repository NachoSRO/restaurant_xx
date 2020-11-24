from django.contrib import admin
from portafolio.receta.models import *
# Register your models here.

class DetalleRecetaInline(admin.StackedInline):
    model = DetalleReceta

class RecetaAdmin(admin.ModelAdmin):
    inlines = [DetalleRecetaInline]

admin.site.register(Receta,RecetaAdmin)