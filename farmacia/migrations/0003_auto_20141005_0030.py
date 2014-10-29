# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0002_turno'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmacia',
            name='descripcion',
            field=models.TextField(help_text=b'Breve Desciripci\xc3\xb3n', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='farmacia',
            name='direccion',
            field=models.CharField(max_length=b'100', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='farmacia',
            name='imagen',
            field=models.ImageField(upload_to=b'farmacia', null=True, verbose_name=b'Seleccionar Imagen'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='farmacia',
            name='telefono',
            field=models.CharField(max_length=b'10', null=True, verbose_name=b'Tel\xc3\xa9fono - Celular'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='farmacia',
            name='tipo',
            field=models.ForeignKey(default=1, to='farmacia.Tipo'),
            preserve_default=True,
        ),
    ]
