#encoding: utf-8

from django.db import models

from django.contrib.auth.models import User
from medicamentos.models import Medicamento

class Tipo(models.Model):
    nombre = models.CharField(max_length='50')

    def __unicode__(self):
        return self.nombre


class Farmacia(models.Model):
    nombre = models.CharField(max_length='100')
    direccion = models.CharField(max_length='100', null=True)
    telefono = models.CharField(max_length='10', verbose_name='Teléfono - Celular', null=True)
    descripcion = models.TextField(help_text='Breve Descripción', null=True)
    imagen = models.ImageField(upload_to='farmacia', verbose_name='Seleccionar Imagen', null=True)
    tipo = models.ForeignKey(Tipo, default=1)
    usuario = models.ForeignKey(User, null=True, blank=True)
    medicamento = models.ManyToManyField(Medicamento, null=True, blank=True, verbose_name='Seleccione sus Medicamentos')
    def __unicode__(self):
        return self.nombre


class Turno(models.Model):
    fecha = models.DateField()
    farmacia = models.ForeignKey(Farmacia, null=True, blank=True)
    def __unicode__(self):
        return self.farmacia.nombre

