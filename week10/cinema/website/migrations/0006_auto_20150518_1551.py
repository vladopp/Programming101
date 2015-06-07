# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_reservations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=50, choices=[('A', 'Action'), ('F', 'Fantasy'), ('C', 'Comedy'), ('D', 'Drama')]),
        ),
    ]
