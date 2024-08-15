from django.utils import timezone
from django.db import models

# Create your models here.
from django.db import models
from datetime import timedelta
from django.utils import timezone

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

    def __str__(self):
        return self.get_nombre_display()


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
    
    def __str__(self):
        return self.get_nombre_display()





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
    
    def __str__(self):
        return f"{self.nombre}"