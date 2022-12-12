
from rest_framework import serializers
from AlumnosMaestria.serializers import SemestreSerializer
from AspirantesMaestria.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username','alumnousuario']


class StatusEntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model:StatusEntrevista
        fields = '__all__'


class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model:Periodo
        fields = '__all__'


class AspiranteSerializer(serializers.ModelSerializer):
    class Meta:
        models:Aspirante
        fields = '__all__'


class ExamenSenevalSerializer(serializers.ModelSerializer):
    class Meta:
        model:ExamenSeneval
        fields = '__all__'


class EstatusRequisitosAspirantesSerializer(serializers.ModelSerializer):
    class Meta:
        model:EstatusRequisitoAspirantes
        fields = '__all__'


class RequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model:Requisito
        fields = '__all__'


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model:Documento
        fields = '__all__'


class DetalleDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model:DetalleDocumento
        fields = '__all__'


class DocenteSerializer(serializers.ModelField):
    class Meta: 
        model:Docente
        fields = '__all__'

class EntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model:Entrevista
        fields = '__all__'


class DetalleEntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model: DetalleEntrevista
        fields = '__all__'


class CatalogoMateriasSerializer(serializers.ModelSerializer):
    class Meta:
        model: CatalogoMaterias
        fields = '__all__'


class CursoPropedeuticoSerializer(serializers.ModelSerializer):
    class Meta:
        model: CursoPropedeutico
        fields = '__all__'


class DetalleAspiranteCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model: DetalleAspiranteCurso
        fields = '__all__'


class CatalogoPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model: CatalogoPregunta
        fields = '__all__'


class EncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model : Encuesta
        fields = '__all__'


class DetalleEncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model : DetalleEncuesta
        fields = '__all__' 

class CriterioSerializer(serializers.ModelSerializer):
    class Meta:
        model : Criterio
        fields = '__all__'


class RubricaSerializer(serializers.ModelSerializer):
    class Meta:
        model:Rubrica
        fields = '__all__'


class DetalleCriterioRubricaSerializer(serializers.ModelSerializer):
    class Meta:
        model:DetalleCriterioRubrica
        fields = '__all__'


class PonenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model:Ponencia
        fields = '__all__'

class DetallePonenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model: DetallePonencia
        fields = '__all__'

