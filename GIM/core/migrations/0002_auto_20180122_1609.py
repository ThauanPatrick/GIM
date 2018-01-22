# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagens',
            name='banda',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='caminho',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='inferior_x',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='inferior_y',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='nuvens',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='orbita',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='projecao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='satelite',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='sensor',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='superior_x',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='superior_y',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='tamanho_pixel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='tipo_banda',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='tipo_imagem',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='xml',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
