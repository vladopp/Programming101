# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150518_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(max_length=40)),
                ('row', models.PositiveSmallIntegerField()),
                ('column', models.PositiveSmallIntegerField()),
                ('projection_id', models.ForeignKey(to='website.Projections')),
            ],
        ),
    ]
