# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'50', null=True, blank=True)),
                ('dosis', models.CharField(max_length=b'50', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'50', null=True, blank=True)),
                ('compuesto', models.ManyToManyField(to='medicamentos.Compuesto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'50', null=True)),
                ('encargado', models.CharField(max_length=b'50', null=True, blank=True)),
                ('telefono', models.CharField(max_length=b'50', null=True, verbose_name=b'Tel\xc3\xa9fono - Celular')),
                ('direccion', models.CharField(max_length=b'50', null=True)),
                ('email', models.EmailField(max_length=75, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'50', null=True, blank=True)),
                ('sigla', models.CharField(max_length=b'50', null=True, blank=True)),
                ('descripcion', models.TextField(help_text=b'Breve Descripcion', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='medicamento',
            name='proveedor',
            field=models.ForeignKey(to='medicamentos.Proveedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compuesto',
            name='unidad',
            field=models.OneToOneField(to='medicamentos.Unidad'),
            preserve_default=True,
        ),
    ]
