from dataclasses import fields
from importlib.metadata import files
from pyexpat import model
from rest_framework import serializers
from AlumnosMaestria.models import DetalleDocumento, Documento, EstatusRequisitoAlumno, Semestre,Periodo,Alumno,Documento,Requisito,CatalogoRequisito
from django.contrib.auth.models import User



class AlumnoSerializers(serializers.ModelSerializer):
    #Usuario = serializers.ReadOnlyField(source='Usuario.username')
    #periodo = serializers.ReadOnlyField(source='periodo.periodo')
    #alumnosemestre=SemestreSerializer(many=False, read_only=True)
    #periodo=PeriodoSerializer(many=False, read_only=True)
    #Usuari=UserSerializer(many=False, read_only=True)
    class Meta:
        model=Alumno
        #fields=['nombre','apellidopaterno','apellidomaterno','curp','email','NumeroControl','alumnosemestre','Usuario','periodo']
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'apellidopaterno': instance.apellidopaterno,
            'apellidomaterno': instance.apellidomaterno,
            'curp': instance.curp,
            'email': instance.email,
            'NumeroControl': instance.NumeroControl,
            'alumnosemestre': {"id": instance.alumnosemestre.pk,"semestre": instance.alumnosemestre.semestre, "descripcion": instance.alumnosemestre.descripcion},
            'Usuario': {"id":instance.Usuario.id,"nombre":instance.Usuario.username},
            'periodo': {"id":instance.periodo.id,"periodo":instance.periodo.periodo}
            # 'face': instance.face
        }

class UserSerializer(serializers.ModelSerializer):
    alumnousuario = AlumnoSerializers(many=False, read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username','alumnousuario']

class SemestreSerializer(serializers.ModelSerializer):
    alumno = AlumnoSerializers(many=True, read_only=True)
    class Meta:
        model = Semestre
        fields = ['id','semestre','descripcion','alumno']

class PeriodoSerializer(serializers.ModelSerializer):
    alumnoperiodo = AlumnoSerializers(many=True)
    class Meta:
        model=Periodo
        fields=['id','periodo',"alumnoperiodo"]
    
class EstatusRequisitosAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstatusRequisitoAlumno
        fields=['nombre','descripcion']

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Documento
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.pk,
            'nombre':instance.nombre,
            'tamaño':instance.tamaño,
            'descripcion':instance.descripcion,
            'requisito':{'id':instance.requisito.id,'nombre':instance.requisito.nombre}
        }

class CatalogoRequisitoSeriazer(serializers.ModelSerializer):
    class Meta:
        model=CatalogoRequisito
        fields='__all__'

class RequisitoSerializer(serializers.ModelSerializer):
    #requisitodocumento = DocumentoSerializer(many=True)
    class Meta:
        model=Requisito
        fields='__all__'
        #fields = ['nombre','descripcion','requisitodocumento']
       # def to_representation(self,instance):
       #     return{
       #         'id': instance.id,
       #         'nombre':instance.nombre,
       #         'descripcion':instance.descripcion,
       #         'requisitodocumento':instance.id,
       #         'catalogo requisito': instance.catalogorequisito
        #    }
    
   

class DetalleDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetalleDocumento
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id':instance.pk,
            'observaciones':instance.observaciones,
            'Fecha carga':instance.carga,
            'ruta': str(instance.ruta),
            'alumno':{'id':instance.alumno.pk,'nombre':instance.alumno.nombre},
            'documento':{'id':instance.documento.pk,'nombre':instance.documento.nombre,'requisito perteneciente':instance.documento.requisito.nombre},
            'estatusrequisito':{'id':instance.estatusrequisitoalumno.pk,'nombre':instance.estatusrequisitoalumno.nombre}
        }
























        