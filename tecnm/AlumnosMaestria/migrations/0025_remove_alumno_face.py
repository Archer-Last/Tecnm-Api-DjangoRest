# Generated by Django 4.0.5 on 2022-10-22 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlumnosMaestria', '0024_alumno_face'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='face',
        ),
    ]
