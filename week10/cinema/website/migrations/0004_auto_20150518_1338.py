# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20150518_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('projection_type', models.CharField(max_length=30)),
                ('projection_date', models.DateField()),
                ('projection_time', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AddField(
            model_name='projections',
            name='movie_id',
            field=models.ForeignKey(to='website.Movie'),
        ),
    ]
