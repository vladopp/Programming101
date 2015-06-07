# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20150518_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projection',
            name='projection_date',
        ),
        migrations.AlterField(
            model_name='projection',
            name='projection_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='projection',
            name='projection_type',
            field=models.SmallIntegerField(choices=[(1, '2D'), (2, '3D'), (3, '4D'), (4, 'IMAX'), (5, 'IMAX 3D'), (6, 'IMAX 4D')]),
        ),
    ]
