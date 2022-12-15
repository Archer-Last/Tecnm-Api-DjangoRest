from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from AlumnosMaestria import views
from AlumnosMaestria.views import * 
from rest_framework import renderers
from rest_framework import routers

# semestre_list = SemestreViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# semestre_detail = SemestreViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# user_list = UserViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# periodo_list = SemestreViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# periodo_detail = SemestreViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# alumno_detail = AlumnoViewset.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# alumno_list = AlumnoViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# estatusrequisito_detail = EstatusRequisitosAlumnoViewset.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# estatusrequisito_list = AlumnoViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# documento_detail = DocumentoViewset.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# documento_list = DocumentoViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# requisito_detail = RequisitoViewset.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# requisito_list = RequisitoViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# detalledocumento_detail =DetalleDocumentoViewset.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# detalledocumento_list = DetalleDocumentoViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# catalogorequisito_detail = CatalogoRequisitoViewset.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# catalogorequisito_list = CatalogoRequisitoViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# app_name = 'AlumnosMaestria'
# urlpatterns = format_suffix_patterns([
 
#     path('', api_root),
#     path('semestre/', semestre_list, name='semestre-list'),
#     path('semestre/<int:pk>/', semestre_detail, name='semestre-detail'),
#     path('periodo/', periodo_list, name='periodo-list'),
#     path('periodo/<int:pk>/', periodo_detail, name='periodo-detail'),
#     path('alumno/',alumno_list, name='alumno-list'),
#     path('alumno/<int:pk>/', alumno_detail, name='alumno-detail'),
#     path('user/', user_list, name='user-list'),
#     path('user/<int:pk>/', user_detail, name='user-detail'),
#     path('estatusrequisito/', estatusrequisito_list, name='estatusrequisito-list'),
#     path('estatusrequisito/<int:pk>/',estatusrequisito_detail, name='estatusrequisito-detail'),
#     path('documentos/',documento_list, name='documento-list'),
#     path('documentos/<int:pk>/',documento_detail, name='documento-detail'),
#     path('requisito/',requisito_list, name='requisito-list'),
#     path('requisito/<int:pk>/',requisito_detail, name='requisito-detail'),
#     path('detalledocumento/',detalledocumento_list, name='detalledocumento-list'),
#     path('detalledocumento/<int:pk>/',detalledocumento_detail, name='detalledocumento-detail'),
#     path('catalogorequisito/',catalogorequisito_list, name='catalogorequisito-list'),
#     path('catalogoquisito/<int:pk>/',catalogorequisito_detail, name='catalogorequisito-detail'),
    
# ])

# urlpatterns = format_suffix_patterns(urlpatterns)


router = routers.DefaultRouter()

#router.register(r'semestre', views.SemestreViewSet)
#router.register(r'periodo', views.PeriodoViewset)
#router.register(r'Alumno', views.AlumnoViewset)
#router.register(r'user', views.UserViewSet)
#router.register(r'estatusrequisito', views.EstatusRequisitosAlumnoViewset)
#router.register(r'documento', views.DocumentoViewset)
#router.register(r'requisito', views.RequisitoViewset)
#router.register(r'detallerequisito', views.DetalleRequisitoViewset)
#router.register(r'catalogorequisito', views.CatalogoRequisitoViewset)

router.register(r'semestre', views.SemestreViewSet,basename="semestre")
router.register(r'periodo', views.PeriodoViewset,basename="periodo")
router.register(r'Alumno', views.AlumnoViewset,basename="Alumno")
router.register(r'user', views.UserViewSet,basename="user")
router.register(r'estatusrequisito', views.EstatusRequisitosAlumnoViewset,basename="estatusrequisito")
router.register(r'documento', views.DocumentoViewset,basename="documentos")
router.register(r'requisito', views.RequisitoViewset,basename="requisitos")
router.register(r'detalledocumento', views.DetalleDocumentoViewset,basename="detalledocumento")
router.register(r'catalogorequisito', views.CatalogoRequisitoViewset,basename="catalogorequisito")
# router.register(r'signup',signup,basename="signup")

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.signup, name= 'signup'),
    path('login/', views.login),

]