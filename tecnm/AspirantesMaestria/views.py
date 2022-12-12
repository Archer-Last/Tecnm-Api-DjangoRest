from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from AspirantesMaestria.serializers import *
from AspirantesMaestria.models import *


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'semestre': reverse('semestre-list', request=request, format=format),
        'StatusEntrevista': reverse('StatusEntrevista-list', request=request, format=format),
        'periodo': reverse('periodo-list', request=request, format=format),
        'aspirante': reverse('aspirante-list', request=request, format=format),
        'examenseneval': reverse('examenseneval-list', request=request, format=format),
        'estatusrequisitoaspirante': reverse('estatusrequisitoaspirante-list', request=request, format=format),
        'requisito': reverse('requisito-list', request=request, format=format),
        'documento': reverse('documento-list', request=request, format=format),
        'detalledocumento': reverse('detalledocumento-list', request=request, format=format),
        'docente': reverse('requisito-list', request=request, format=format),
        'entrevista': reverse('entrevista-list', request=request, format=format),
        'detalleentrevista': reverse('dealleentrevista-list', request=request, format=format),
        'catalogomaterias': reverse('catalogomaterias-list', request=request, format=format),
        'cursopropedeutico': reverse('cursopropedeutico-list', request=request, format=format),
        'detalleaspirantescurso': reverse('detalleaspirantescurso-list', request=request, format=format),
        'catalogopregunta': reverse('catalogopregunta-list', request=request, format=format),
        'encuesta': reverse('encuesta-list', request=request, format=format),
        'detalleencuesta': reverse('detalleencuesta-list', request=request, format=format),
        'criterio': reverse('criterio-list', request=request, format=format),
        'rubrica': reverse('rubrica-list', request=request, format=format),
        'detallecriterio': reverse('detallecriterio-list', request=request, format=format),
        'ponencia': reverse('ponencia-list', request=request, format=format),
        'detalleponencia': reverse('detalleponencia-list', request=request, format=format),

    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StatusEntrevistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StatusEntrevista.objects.all()
    serializer_class = StatusEntrevistaSerializer


class PeriodoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer


class AspiranteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Aspirante.objects.all()
    serializer_class = AspiranteSerializer


class ExamenSenevalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExamenSeneval.objects.all()
    serializer_class = ExamenSenevalSerializer


class EstatusRequisitoAspiranteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstatusRequisitoAspirantes.objects.all()
    serializer_class = EstatusRequisitosAspirantesSerializer


class RequisitoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Requisito.objects.all()
    serializer_class = RequisitoSerializer


class DocumentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


class DetalleDocumentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetalleDocumento.objects.all()
    serializer_class = DetalleDocumentoSerializer


class DocenteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer


class EntrevistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entrevista.objects.all()
    serializer_class = EntrevistaSerializer


class DetalleEntrevistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetalleEntrevista.objects.all()
    serializer_class = DocumentoSerializer


class CatalogoMateriasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CatalogoMaterias.objects.all()
    serializer_class = CatalogoMateriasSerializer


class CursoPropedeuticoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CursoPropedeutico.objects.all()
    serializer_class = CursoPropedeuticoSerializer


class DetalleAspirantesCursoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetalleAspiranteCurso.objects.all()
    serializer_class = DetalleAspiranteCursoSerializer


class CatalogoPreguntaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CatalogoPregunta.objects.all()
    serializer_class = CatalogoPreguntaSerializer


class EncuestaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer


class DetalleEncuestaiewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetalleEncuesta.objects.all()
    serializer_class = DetalleEncuestaSerializer


class CriterioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Criterio.objects.all()
    serializer_class = CriterioSerializer


class RubricaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rubrica.objects.all()
    serializer_class = RubricaSerializer


class DetalleCriterioRubricaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetalleCriterioRubrica.objects.all()
    serializer_class = DetalleCriterioRubricaSerializer


class PonenciaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ponencia.objects.all()
    serializer_class = PonenciaSerializer


class DetallePonenciaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetallePonencia.objects.all()
    serializer_class = DetallePonencia


