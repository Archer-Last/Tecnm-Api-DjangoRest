# Generated by Django 4.0.5 on 2022-10-14 19:36

import AlumnosMaestria.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumnosMaestria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='ruta',
            field=models.FileField(upload_to=AlumnosMaestria.models.user_directory_path),
        ),
    ]
