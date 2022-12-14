from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from  AlumnosMaestria.urls import router as router_AlumnosMaestria
from  AspirantesMaestria.urls import router as router_AspirantesMaestria
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

class DefaultRouter(routers.DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for
    extending url routes from another router.
    """
    def extend(self, router):
        """
        Extend the routes with url routes of the passed in router.
 
        Args:
             router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(router.registry)


RouterAspirantes = DefaultRouter()
RouterAspirantes.extend(router_AspirantesMaestria)


RouterAlumnos = DefaultRouter()
RouterAlumnos.extend(router_AlumnosMaestria)


# Create a router and register our viewsets with it.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    # path('', include(RouterAlumnos.urls)),
    # # path('Alumnos/',include(RouterAlumnos.urls)),
    path('Alumno/',include(RouterAlumnos.urls)),
    # path('Aspirantes/', include(RouterAspirantes.urls)),
    path('Alumnos/', include('AlumnosMaestria.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token)
]

if settings.DEBUG == True:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)