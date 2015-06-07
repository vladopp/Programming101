# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20150518_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('projection_type', models.CharField(max_length=20, choices=[('1', '2D'), ('2', '3D'), ('3', '4D'), ('4', 'IMAX'), ('5', 'IMAX 3D'), ('6', 'IMAX 4D')])),
                ('projection_date', models.DateField()),
                ('projection_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('username', models.CharField(max_length=40)),
                ('row', models.PositiveSmallIntegerField()),
                ('column', models.PositiveSmallIntegerField()),
                ('projection_id', models.ForeignKey(to='website.Projection')),
            ],
        ),
        migrations.RemoveField(
            model_name='projections',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='projection_id',
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(verbose_name='Movie name', max_length=100),
        ),
        migrations.DeleteModel(
            name='Projections',
        ),
        migrations.DeleteModel(
            name='Reservations',
        ),
        migrations.AddField(
            model_name='projection',
            name='movie_id',
            field=models.ForeignKey(to='website.Movie'),
        ),
    ]
