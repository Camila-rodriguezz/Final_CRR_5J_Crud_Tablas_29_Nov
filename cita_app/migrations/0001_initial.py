# Generated by Django 5.1.3 on 2024-11-26 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id_cita', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('fecha_cita', models.DateField()),
                ('hora_cita', models.CharField(max_length=100)),
                ('id_cliente', models.CharField(max_length=100)),
                ('id_empleado', models.CharField(max_length=100)),
                ('servicio', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
    ]