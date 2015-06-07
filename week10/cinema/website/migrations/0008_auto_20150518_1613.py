# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20150518_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projections',
            name='projection_type',
            field=models.CharField(choices=[('1', '2D'), ('2', '3D'), ('3', '4D'), ('4', 'IMAX'), ('5', 'IMAX 3D'), ('6', 'IMAX 4D')], max_length=20),
        ),
    ]
