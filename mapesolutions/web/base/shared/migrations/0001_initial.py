# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-20 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medico_id', models.IntegerField()),
                ('nome_medico', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('valor', models.FloatField()),
            ],
            options={
                'ordering': ['valor'],
            },
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField()),
                ('valor', models.FloatField()),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.Consulta')),
            ],
        ),
    ]
