# Generated by Django 4.0.5 on 2022-08-31 18:50

import AspirantesMaestria.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirante',
            fields=[
                ('idaspirante', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidopaterno', models.CharField(max_length=45)),
                ('apellidomaterno', models.CharField(max_length=45)),
                ('curp', models.CharField(max_length=18, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('Usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoMaterias',
            fields=[
                ('idMateria', models.AutoField(primary_key=True, serialize=False)),
                ('Materia', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoPregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pregunta', models.CharField(max_length=200)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Criterio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CursoPropedeutico',
            fields=[
                ('idcurso', models.AutoField(primary_key=True, serialize=False)),
                ('FechaInicio', models.DateField()),
                ('FechaFinalizacion', models.DateField()),
                ('HoraInicio', models.TimeField()),
                ('HoraFinalizacion', models.TimeField()),
                ('Clave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.catalogomaterias')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCriterioRubrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('Descripcion', models.CharField(max_length=400)),
                ('criterio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.criterio')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleEncuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Respuesta', models.CharField(blank=True, max_length=150, null=True)),
                ('catalogopreguntas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.catalogopregunta')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleEntrevista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePonencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Valor', models.IntegerField(null=True)),
                ('criterio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.criterio')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleRequisito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta', models.FileField(blank=True, null=True, upload_to=AspirantesMaestria.models.user_directory_path)),
                ('carga', models.DateTimeField(blank=True, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=85, null=True)),
                ('aspirante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.aspirante')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=45)),
                ('ApellidoPaterno', models.CharField(max_length=45)),
                ('ApellidoMaterno', models.CharField(max_length=45)),
                ('Curp', models.CharField(max_length=18, unique=True)),
                ('Rfc', models.CharField(max_length=13, unique=True)),
                ('CedulaProfesional', models.CharField(max_length=8, unique=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EstatusAspirante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=85)),
            ],
        ),
        migrations.CreateModel(
            name='EstatusRequisitoEstudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=85)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StatusEntrevista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estatus', models.CharField(max_length=45)),
                ('Descripcion', models.CharField(blank=True, max_length=85, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rubrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rubrica', models.CharField(max_length=50)),
                ('detallecriteriorubricas', models.ManyToManyField(through='AspirantesMaestria.DetalleCriterioRubrica', to='AspirantesMaestria.criterio')),
            ],
        ),
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90)),
                ('descripcion', models.CharField(max_length=300)),
                ('tamaño', models.DecimalField(decimal_places=2, max_digits=4)),
                ('detalle', models.ManyToManyField(through='AspirantesMaestria.DetalleRequisito', to='AspirantesMaestria.aspirante')),
            ],
        ),
        migrations.CreateModel(
            name='Ponencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaHora', models.DateTimeField(blank=True, null=True)),
                ('Observaciones', models.CharField(blank=True, max_length=100, null=True)),
                ('Documento', models.FileField(blank=True, null=True, upload_to=AspirantesMaestria.models.user_directory_path3)),
                ('detallePonencia', models.ManyToManyField(through='AspirantesMaestria.DetallePonencia', to='AspirantesMaestria.criterio')),
                ('detalleentrevista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.detalleentrevista', unique=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.statusentrevista')),
            ],
        ),
        migrations.CreateModel(
            name='ExamenSeneval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ICNE', models.IntegerField()),
                ('PMA', models.IntegerField()),
                ('PAN', models.IntegerField()),
                ('ELE', models.IntegerField()),
                ('CLE', models.IntegerField()),
                ('MET', models.IntegerField()),
                ('ICL', models.IntegerField()),
                ('IUG', models.IntegerField()),
                ('aspirante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.aspirante')),
            ],
        ),
        migrations.CreateModel(
            name='Entrevista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('HoraInicio', models.TimeField()),
                ('HoraFinal', models.TimeField()),
                ('Observaciones', models.CharField(blank=True, max_length=45, null=True)),
                ('aspirante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.aspirante')),
                ('detalleentrevistas', models.ManyToManyField(through='AspirantesMaestria.DetalleEntrevista', to='AspirantesMaestria.docente')),
            ],
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaHora', models.DateTimeField(blank=True, null=True)),
                ('Observaciones', models.CharField(blank=True, max_length=100, null=True)),
                ('Documento', models.FileField(blank=True, null=True, upload_to=AspirantesMaestria.models.user_directory_path2)),
                ('detalleEncuesta', models.ManyToManyField(through='AspirantesMaestria.DetalleEncuesta', to='AspirantesMaestria.catalogopregunta')),
                ('detalleentrevista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.detalleentrevista', unique=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.statusentrevista')),
            ],
        ),
        migrations.AddField(
            model_name='detallerequisito',
            name='estatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.estatusrequisitoestudiante'),
        ),
        migrations.AddField(
            model_name='detallerequisito',
            name='requisito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.requisito'),
        ),
        migrations.AddField(
            model_name='detalleponencia',
            name='ponencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.ponencia'),
        ),
        migrations.AddField(
            model_name='detalleentrevista',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.docente'),
        ),
        migrations.AddField(
            model_name='detalleentrevista',
            name='entrevista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.entrevista'),
        ),
        migrations.AddField(
            model_name='detalleencuesta',
            name='encuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.encuesta'),
        ),
        migrations.AddField(
            model_name='detallecriteriorubrica',
            name='rubrica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.rubrica'),
        ),
        migrations.CreateModel(
            name='DetalleAspiranteCurso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Calificacion', models.IntegerField()),
                ('aspirante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.aspirante')),
                ('cursopropedeutico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.cursopropedeutico')),
            ],
        ),
        migrations.AddField(
            model_name='cursopropedeutico',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.docente'),
        ),
        migrations.AddField(
            model_name='cursopropedeutico',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.periodo'),
        ),
        migrations.AddField(
            model_name='aspirante',
            name='estatusaspirante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.estatusaspirante'),
        ),
        migrations.AddField(
            model_name='aspirante',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AspirantesMaestria.periodo'),
        ),
        migrations.AddIndex(
            model_name='detalleentrevista',
            index=models.Index(fields=['entrevista', 'docente'], name='AspirantesM_entrevi_25ab6c_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='detalleentrevista',
            unique_together={('entrevista', 'docente')},
        ),
        migrations.AddIndex(
            model_name='detallecriteriorubrica',
            index=models.Index(fields=['criterio', 'rubrica'], name='AspirantesM_criteri_75d9d6_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='detallecriteriorubrica',
            unique_together={('criterio', 'rubrica')},
        ),
        migrations.AddIndex(
            model_name='detalleaspirantecurso',
            index=models.Index(fields=['aspirante', 'cursopropedeutico'], name='AspirantesM_aspiran_154323_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='detalleaspirantecurso',
            unique_together={('aspirante', 'cursopropedeutico')},
        ),
    ]