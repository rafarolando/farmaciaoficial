# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0005_auto_20141013_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmacia',
            name='medicamento',
            field=models.ManyToManyField(to=b'medicamentos.Medicamento', null=True, blank=True),
        ),
    ]
