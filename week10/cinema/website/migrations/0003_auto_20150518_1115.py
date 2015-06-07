# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150518_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
