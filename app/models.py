from django.utils import timezone
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.
from django.db import models
from datetime import timedelta
from django.utils import timezone


class ImagenProducto(models.Model):
    """
    Fotos de producto, compartidas por los cuatro modelos de catálogo.
    En vez de agregar tres campos de imagen repetidos en cada modelo
    (Teclado, Mouse, Auricular, Mousepad), esta tabla se engancha a
    cualquiera de los cuatro a través de una relación genérica — el
    mismo espíritu del resto del proyecto: una sola pieza reutilizada
    por tipo de producto, en vez de una por cada uno.
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    producto = GenericForeignKey('content_type', 'object_id')
    imagen = models.ImageField(upload_to='productos/')
    orden = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['orden', 'id']

    def __str__(self):
        return f"Imagen #{self.orden} de {self.producto}"


class Teclado(models.Model):
    TIPOS_DE_TECLADO = [
        ('membrana', 'Membrana'),
        ('mecanico', 'Mecanico'),
        ('semimecanico', 'SemiMecanico'),
    ]

    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=20, choices=TIPOS_DE_TECLADO, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=False)
    imagenes = GenericRelation(ImagenProducto)

    def __str__(self):
        return self.nombre


class Mouse(models.Model):
    TIPOS_DE_MOUSE = [
        ('optico', 'Optico'),
        ('inalambrico', 'Inalambrico'),
        ('gaming', 'Gaming'),
    ]

    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=20, choices=TIPOS_DE_MOUSE, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=False)
    imagenes = GenericRelation(ImagenProducto)
    

    def __str__(self):
        return f"{self.nombre}"


class Auricular(models.Model):
    TIPOS_DE_AURICULAR = [
        ('cable', 'Cable'),
        ('inalambrico', 'Inalambrico'),
        ('gaming', 'Gaming'),
    ]

    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=20, choices=TIPOS_DE_AURICULAR, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=False)
    imagenes = GenericRelation(ImagenProducto)

    def __str__(self):
        return self.nombre



class Mousepad(models.Model):
    TIPOS_DE_MOUSEPAD = [
        ('tela', 'Tela'),
        ('vidrio', 'Vidrio'),
        ('gaming', 'Gaming'),
    ]

    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=20, choices=TIPOS_DE_MOUSEPAD, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=False)
    imagenes = GenericRelation(ImagenProducto)
    
    def __str__(self):
        return f"{self.nombre}"