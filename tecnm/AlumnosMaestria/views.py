from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import *
from rest_framework import viewsets
from AlumnosMaestria.serializers import *
from AlumnosMaestria.models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import *
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate



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


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request) # data is a dictionary
            user = User.objects.create_user(username=data['username'],email=data['email'],password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)},status=201)
        except IntegrityError:
            return JsonResponse( {'error':'username taken. choose another username'},status=400)


@csrf_exempt
def login(request): 
    if request.method == 'POST':
        data = JSONParser().parse(request) 
        user = authenticate(request,username=data['username'],password=data['password'])
    if user is None:
        return JsonResponse(
            {'error':'unable to login. check username and password'},status=400)
    else: # return user token
        try:
            token = Token.objects.get(user=user)
        except: # if token not in db, create a new one
            token = Token.objects.create(user=user)
        return JsonResponse({'token':str(token)}, status=201)