from django.db import models
from portafolio.producto.models import *
# Create your models here.

class Receta(models.Model):
    TIPO = (
        ('postre', 'Postre'),
        ('bebida','Bebida'),
        ('plato','Plato'),
    )
    nombre = models.CharField('Nombre',unique = True, max_length=100)
    descripcion = models.CharField('descripcion',max_length=500)
    tipo = models.CharField(choices=TIPO, max_length=30,null=True)
    precio = models.PositiveSmallIntegerField(default=1,verbose_name="precio")

    class Meta:
        db_table = 'Receta'
    
    def __str__(self):
        return self.nombre

class DetalleReceta(models.Model):
    receta_id = models.ForeignKey(Receta,on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField(default=1,verbose_name="cantidad")