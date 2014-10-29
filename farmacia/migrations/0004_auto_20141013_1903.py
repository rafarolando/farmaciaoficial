# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0001_initial'),
        ('farmacia', '0003_auto_20141005_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmacia',
            name='medicamento',
            field=models.ManyToManyField(to='medicamentos.Medicamento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='farmacia',
            name='descripcion',
            field=models.TextField(help_text=b'Breve Descripci\xc3\xb3n', null=True),
        ),
    ]
