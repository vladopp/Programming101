# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20150518_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='raiting',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='projections',
            name='projection_type',
            field=models.CharField(choices=[(1, '2D'), (2, '3D'), (3, '4D'), (4, 'IMAX'), (5, 'IMAX 3D'), (6, 'IMAX 4D')], max_length=20),
        ),
    ]
