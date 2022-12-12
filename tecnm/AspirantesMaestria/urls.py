from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from AspirantesMaestria import views
from AspirantesMaestria.views import * 
from rest_framework import renderers
from rest_framework import routers


statusentrevistas_list = StatusEntrevistaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
statusentrevista_detail = StatusEntrevistaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



periodo_list = PeriodoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
periodo_detail = PeriodoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



aspirante_list = AspiranteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
aspirante_detail = AspiranteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



examenseneval_list = ExamenSenevalViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
examenseneval_detail = ExamenSenevalViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



estatusrequisitosaspirantes_list = EstatusRequisitoAspiranteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
estatusrequisitosaspirantes_detail = EstatusRequisitoAspiranteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



requisito_list = RequisitoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
requisito_detail = RequisitoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



documento_list = DocumentoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
documento_detail = DocumentoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



detalledocumento_list = DetalleDocumentoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
detalledocumento_detail = DetalleDocumentoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



docente_list = DocenteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
docente_detail = DocenteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



entrevista_list = EntrevistaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
entrevista_detail = EntrevistaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



detalleentrevista_list = DetalleEntrevistaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
detalleentrevista_detail = DetalleEntrevistaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



catalogomaterias_list = CatalogoMateriasViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
catalogomaterias_detail = CatalogoMateriasViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



cursopropedeutico_list = CursoPropedeuticoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
cursopropedeutico_detail = CursoPropedeuticoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



detalleaspirantescurso_list = DetalleAspirantesCursoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
aetalleaspirantescurso_detail = DetalleAspirantesCursoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



catalogopregunta_list = CatalogoPreguntaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
catalogopregunta_detail = CatalogoPreguntaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



encuesta_list = EncuestaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
encuesta_detail = EncuestaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



detalleencuesta_list = DetalleEncuestaiewSet.as_view({
    'get': 'list',
    'post': 'create'
})
detalleencuesta_detail = DetalleEncuestaiewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



criterio_list = CriterioViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
criterio_detail = CriterioViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



rubrica_list = RubricaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
rubrica_detail = RubricaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



detallecriteriorubrica_list = DetalleCriterioRubricaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
detallecriteriorubrica_detail = DetalleCriterioRubricaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



ponencia_list = PonenciaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
ponencia_detail = PonenciaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



detalleponencia_list = DetallePonenciaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
detalleponencia_detail = DetallePonenciaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


app_name = 'AspirantesMaestria'
urlpatterns = [
 
    path('', api_root),
    path('user/', user_list, name='user-list'),
    path('user/<int:pk>/', user_detail, name='user-detail'),
    path('statusentrevista/', statusentrevistas_list, name='statusentrevistas-list'),
    path('statusentrevista/<int:pk>/', statusentrevista_detail, name='statusentrevistas-detail'),
    path('periodo/', periodo_list, name='periodo-list'),
    path('periodo/<int:pk>/', periodo_detail, name='periodo-detail'),
    path('aspirante/',aspirante_list, name='aspirante-list'),
    path('aspirante/<int:pk>/', aspirante_detail, name='aspirante-detail'),
    path('examenseneval/', examenseneval_list, name='examenseneval-list'),
    path('examenseneval/<int:pk>/',examenseneval_detail, name='examenseneval-detail'),
    path('estatusrequisitosaspirantes/',estatusrequisitosaspirantes_list, name='estatusrequisitosaspirantes-list'),
    path('estatusrequisitosaspirantes/<int:pk>/',estatusrequisitosaspirantes_detail, name='estatusrequisitosaspirantes-detail'),
    path('documento/',documento_list, name='documento-list'),
    path('documento/<int:pk>/',documento_detail, name='documento-detail'),
    path('requisito/',requisito_list, name='requisito-list'),
    path('requisito/<int:pk>/',requisito_detail, name='requisito-detail'),
    path('detalledocumento/',detalledocumento_list, name='detalledocumento-list'),
    path('detalledocumento/<int:pk>/',detalledocumento_detail, name='detalledocumento-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)


router = routers.SimpleRouter()
router.register(r'documento', views.DocumentoViewSet)
router.register(r'requisito', views.RequisitoViewSet)