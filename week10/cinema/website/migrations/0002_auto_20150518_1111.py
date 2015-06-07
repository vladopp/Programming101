# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='length',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
