# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-27 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recurso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='estadoReserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='listaReserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.TextField(max_length=50)),
                ('fecha_fin', models.TextField(max_length=50)),
                ('gano_reserva', models.NullBooleanField()),
                ('estado_reserva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reserva.estadoReserva')),
                ('lista_reserva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reserva.listaReserva')),
                ('recurso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recurso.recurso')),
                ('tipo_recurso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recurso.Tipo_de_recurso')),
            ],
            options={
                'permissions': (('ver_reserva', 'Puede ver las reservas disponibles'),),
            },
        ),
    ]