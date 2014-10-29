#encoding:UTF-8

from django.db import models

from django.contrib.auth.models import User


class Proveedor (models.Model):
    nombre = models.CharField(max_length='50', null=True)
    encargado = models.CharField(max_length='50', null=True, blank=True)
    telefono = models.CharField(max_length='50', verbose_name='Teléfono - Celular', null=True)
    direccion = models.CharField(max_length='50', null= True)
    email = models.EmailField(null = True)

    def __unicode__(self):
        return self.nombre

class Unidad (models.Model):
    nombre = models.CharField(max_length='50', null=True, blank=True)
    sigla = models.CharField(max_length='50', null=True, blank=True)
    descripcion = models.TextField(help_text='Breve Descripcion', null=True)

    def __unicode__(self):
        return self.sigla

class Compuesto(models.Model):
    nombre = models.CharField(max_length='50', null=True, blank=True)
    dosis = models.CharField(max_length='50', null=True, blank=True)
    unidad = models.OneToOneField(Unidad)


    def __unicode__(self):
        return self.nombre

class Medicamento(models.Model):
    nombre = models.CharField(max_length='50', null= True, blank=True)
    proveedor = models.ForeignKey(Proveedor)
    compuesto = models.ManyToManyField(Compuesto)

    def __unicode__(self):
        return  self.nombre

