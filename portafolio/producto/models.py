from django.db import models
from django.core.validators import MinValueValidator
import decimal
import datetime
from django.utils.timezone import now
# Create your models here.

########## PRODUCTO #################
class Producto(models.Model):
    TIPO = (
        ('fruta', 'Fruta'),
        ('verdura', 'Verdura'),
        ('pastas','Pastas'),
        ('bebidas','Bebidas'),
        ('bebidas Alcoholicas','Bebidas Alcoholicas'),
        ('utensilio','Utensilio'),
        ('carnes rojas','Carnes Rojas'),
        ('carnes blancas','Carnes Blancas'),
        ('arroz','Arroz'),
        ('postre','Postre'),
        ('lacteo','Lacteos'),
        ('pan','Pan'),
        ('condimento','Condimento'),
        ('bebedas','Bebidas')

    )
    GRAMAJE = (
        ('ml','ML'),
        ('gr','Gr'),
        ('unidad','Unidad'),

    )
    cod_producto = models.CharField(max_length=150,unique=True,verbose_name="Codigo Producto")
    name = models.CharField(max_length=150,verbose_name="Nombre Producto",unique=True)
    tipo = models.CharField(choices=TIPO, max_length=30,null=True)
    precio_Compra = models.PositiveSmallIntegerField(default=1,verbose_name="Precio de compra")
    stock = models.PositiveSmallIntegerField(default=1,verbose_name="Stock",
            validators=[MinValueValidator(1)])
    gramaje = models.CharField(choices=GRAMAJE, max_length=30,null=True)
    descripcion = models.TextField(max_length=400,verbose_name="Descripcion del producto")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Producto'
        ordering = ['cod_producto']

######### PROVEEDOR ###################
class Proveedor(models.Model):
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedor"
        db_table = 'Proveedor'

    rut = models.CharField(unique=True,null=True,max_length=10)
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=9, verbose_name="Teléfono")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")

    def __str__(self):
        return self.nombre

######## SOLICITUD DE PEDIDO ##############
class SolicitudProducto(models.Model):
    codigo = models.IntegerField(unique=True, verbose_name="Código Solicitud")
    fecha_solicitud = models.DateTimeField(default=now,blank=True)
    estado = models.BooleanField(default = False)

    class Meta:
        db_table = 'SolicitudProducto'

class DetalleSolicitudProd(models.Model):
    solicitud_producto = models.ForeignKey(SolicitudProducto,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField(default=1,verbose_name="cantidad")

    class Meta:
        db_table = 'DetalleSolicitudProd'

####################     PEDIDO ###################################
class IngresoPedidoProd(models.Model):
    codigo = models.IntegerField(unique=True, verbose_name="Código")
    fecha_ingreso = models.DateField(null=True,blank=True)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'IngresoPedido_prod'
    
    def __str__(self):
        return f'{self.codigo}'

class FacturaPedidoProd(models.Model):
    ingreso_producto = models.ForeignKey(IngresoPedidoProd,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField(default=1,verbose_name="cantidad")

    class Meta:
        db_table = 'FacturaPedido_prod'

    

