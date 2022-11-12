from django.urls import include, path
from rest_framework import routers
from proyectos.views.rol import *

router = routers.DefaultRouter()
router.register(r'rol', RolViewSet)
# router.register(r'regional', RegionalViewSet)
# router.register(r'ficha', FichaViewSet)
# router.register(r'centro', CentroViewSet)
# router.register(r'programa', ProgramaViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]