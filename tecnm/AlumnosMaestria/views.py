from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from AlumnosMaestria.serializers import *
from AlumnosMaestria.models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'semestre': reverse('semestre-list', request=request, format=format),
        'periodo': reverse('periodo-list', request=request, format=format),
        'alumno': reverse('alumno-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'requisito': reverse('requisito-list', request=request, format=format),
        'documento': reverse('documento-list', request=request, format=format),
        'detallerequisito': reverse('detallerequisito-list', request=request, format=format),
        'estatusrequisito': reverse('estatusrequisito-list', request=request, format=format),
        'catalogorequisito': reverse('catalogorequisito-list', request=request, format=format)
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SemestreViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Semestre.objects.all()
    serializer_class = SemestreSerializer

class PeriodoViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer

class AlumnoViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializers

class EstatusRequisitosAlumnoViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = EstatusRequisitoAlumno.objects.all()
    serializer_class = EstatusRequisitosAlumnoSerializer

class RequisitoViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Requisito.objects.all()
    serializer_class = RequisitoSerializer

class DocumentoViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class DetalleDocumentoViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DetalleDocumento.objects.all()
    serializer_class = DetalleDocumentoSerializer

class CatalogoRequisitoViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CatalogoRequisito.objects.all()
    serializer_class = CatalogoRequisitoSeriazer
    