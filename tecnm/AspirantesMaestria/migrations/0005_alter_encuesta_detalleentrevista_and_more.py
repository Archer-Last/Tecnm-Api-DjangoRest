# Generated by Django 4.0.5 on 2022-09-08 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AspirantesMaestria', '0004_rename_requisito_detalledocumento_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='detalleentrevista',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.detalleentrevista'),
        ),
        migrations.AlterField(
            model_name='ponencia',
            name='detalleentrevista',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.detalleentrevista'),
        ),
    ]