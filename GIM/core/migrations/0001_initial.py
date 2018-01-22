# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banda', models.IntegerField()),
                ('superior_x', models.IntegerField()),
                ('superior_y', models.IntegerField()),
                ('inferior_x', models.IntegerField()),
                ('inferior_y', models.IntegerField()),
                ('tipo_banda', models.CharField(max_length=10)),
                ('tamanho_pixel', models.IntegerField()),
                ('projecao', models.CharField(max_length=255)),
                ('tipo_imagem', models.CharField(max_length=20)),
                ('nuvens', models.IntegerField()),
                ('satelite', models.CharField(max_length=20)),
                ('sensor', models.CharField(max_length=20)),
                ('data', models.DateField()),
                ('orbita', models.IntegerField()),
                ('caminho', models.CharField(max_length=255)),
                ('nome', models.CharField(max_length=100)),
                ('xml', models.CharField(max_length=100)),
            ],
        ),
    ]
