# Generated by Django 4.0.5 on 2022-10-14 19:48

import AlumnosMaestria.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumnosMaestria', '0023_remove_alumno_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='face',
            field=models.FileField(default='PORTADA.png', upload_to=AlumnosMaestria.models.user_directory_path),
            preserve_default=False,
        ),
    ]
