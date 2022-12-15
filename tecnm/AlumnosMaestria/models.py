from tkinter import CASCADE
from django.db import models
from django.db.models.base import Model
from django.dispatch import receiver
import os
from django.db.models.signals import post_delete, pre_save, post_save
from django.contrib.auth.models import User
import re

from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class Semestre(models.Model):
    semestre=models.CharField(max_length=45, null=False)
    descripcion=models.CharField(max_length=85, null=False)
    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.semestre
    


class Periodo(models.Model):
    periodo=models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.periodo


#Se agrego un atributo para poder cargar la una imagen de 
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Alumnos/user_{0}_{1}/{2}'.format( re.sub(r"[^a-zA-Z0-9.]","", str(instance.Usuario)), re.sub(r"[^a-zA-Z0-9.]","",str(instance.nombre+" "+instance.apellidopaterno+" "+instance.apellidomaterno)), re.sub(r"[^a-zA-Z0-9.]","",str(filename)) )

class Alumno(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    apellidopaterno = models.CharField(max_length=45,null=False)
    apellidomaterno = models.CharField(max_length=45,null=False)
    curp= models.CharField(max_length=18,null=False,unique=True)
    email= models.EmailField(unique=True)
    NumeroControl=models.CharField(max_length=15,null=False, unique=True)
    alumnosemestre = models.ForeignKey(Semestre, related_name='alumno',on_delete=models.CASCADE)
    Usuario= models.OneToOneField(User,related_name='alumnousuario', on_delete=models.CASCADE,null=True)
    periodo=models.ForeignKey(Periodo, related_name='alumnoperiodo',on_delete=models.CASCADE,null=True)
    # face = models.FileField(upload_to=user_directory_path ,null=False)
    def __str__(self):
        return self.nombre + " "+ self.apellidopaterno + " " + self.apellidomaterno


@receiver(models.signals.post_delete, sender=Alumno)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Elimina el archivo de directorio si se elimina el objeto correspondiente.
    """ 
    if instance.ruta:
        if os.path.isfile(instance.ruta.path):
            print("path: ", instance.ruta.path)
            os.remove(instance.ruta.path)

 

@receiver(models.signals.pre_save, sender=Alumno)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Elimina el archivo antiguo del directorio cuando se actualiza el objeto correspondiente con un nuevo archivo
    """
    if not instance.pk:
        return False

    old_file = sender.objects.get(pk=instance.pk).ruta

    if old_file:
        new_file = instance.ruta
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    else:
        pass



class EstatusRequisitoAlumno(models.Model):
    nombre = models.CharField(max_length=45, null=False) 
    descripcion = models.CharField(max_length=85,null=False)
    def __str__(self):
        return self.nombre

#Este modelo tabla de registro fue propuesta por el director del proyecto. tiene como proposito clasificar los requisitos para su posterior filtrado
class CatalogoRequisito(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    descripcion = models.CharField(max_length=300,blank=True, null=True)
    def __str__(self):
        return self.nombre

#La tabla requisito esuna nueva tabla creada con la necesidad de agrupar multiples documentos, bajo una uniodad de requisito. esto basad0o en la logica de negocios de la empreza a la que esta destinada el sistema. 
class Requisito(models.Model):
    nombre= models.CharField(max_length=100,null=False)
    descripcion = models.CharField(max_length=600,null=True)
    semestre= models.ForeignKey(Semestre, on_delete=models.CASCADE,null=True)
    catalogorequisito = models.ForeignKey(CatalogoRequisito,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nombre

#La tabla Documento en un principio fue consebida como tabla Requisitos, las posteriores necesidades del sistema llavaron a renombrarla, conservando su fumcion en su totalidad
class Documento(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=600, null= True)
    detalle = models.ManyToManyField(Alumno, through='DetalleDocumento')
    requisito = models.ForeignKey(Requisito,related_name='requisitodocumento', on_delete=models.CASCADE, null=True)
    tamaño=models.DecimalField(null=False, max_digits=4, decimal_places=2)
    
    def __str__(self):
        return self.nombre

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Alumnos/user_{0}_{1}/{2}'.format( re.sub(r"[^a-zA-Z0-9.]","", str(instance.alumno.Usuario)), re.sub(r"[^a-zA-Z0-9.]","",str(instance.alumno)), re.sub(r"[^a-zA-Z0-9.]","",str(filename)) )

# Se cambio el nombre del modelo por razones de integridad con lo nuevos camnios
class DetalleDocumento(models.Model):
    ruta = models.FileField(upload_to=user_directory_path ,null=True)
    observaciones = models.CharField(max_length=95,blank=True, null=True)
    carga=models.DateTimeField(blank=True,null=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE,null=True)
    estatusrequisitoalumno = models.ForeignKey(EstatusRequisitoAlumno, on_delete=models.CASCADE) 


@receiver(models.signals.post_delete, sender=DetalleDocumento)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Elimina el archivo de directorio si se elimina el objeto correspondiente.
    """ 
    if instance.ruta:
        if os.path.isfile(instance.ruta.path):
            print("path: ", instance.ruta.path)
            os.remove(instance.ruta.path)

 

@receiver(models.signals.pre_save, sender=DetalleDocumento)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Elimina el archivo antiguo del directorio cuando se actualiza el objeto correspondiente con un nuevo archivo
    """
    if not instance.pk:
        return False

    old_file = sender.objects.get(pk=instance.pk).ruta

    if old_file:
        new_file = instance.ruta
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    else:
        pass






@receiver(post_save, sender=Documento, dispatch_uid="update_stock_count") 
def update_requisito(sender, instance, **kwargs):


    my_objects = list(DetalleDocumento.objects.filter(requisito=instance))
    if not my_objects:
        statusR = EstatusRequisitoAlumno.objects.get(pk=1)
    
        ListaAlumno = Alumno.objects.all()
        for alumno01 in ListaAlumno:
             detalle = DetalleDocumento.objects.create(alumno=alumno01,requisito=instance,estatusrequisitoalumno=statusR,observaciones=" ")
        detalle.save()     

    post_save.disconnect(update_requisito, sender=Documento)
    post_save.connect(update_requisito, sender=Documento)


@receiver(post_save, sender=Alumno, dispatch_uid="update_Alumno_count") 
def New_Alumno(sender, instance, **kwargs):


    my_objects = list(DetalleDocumento.objects.filter(alumno=instance))
    if not my_objects:
        statusR = EstatusRequisitoAlumno.objects.get(pk=1)
    
        ListaDocumentos = Documento.objects.all()
        for documentoN in ListaDocumentos:
             detalle = DetalleDocumento.objects.create(alumno=instance,documento=documentoN,estatusrequisitoalumno=statusR,observaciones=" ")
        detalle.save()     

    post_save.disconnect(New_Alumno, sender=Alumno)
    post_save.connect(New_Alumno, sender=Alumno)
