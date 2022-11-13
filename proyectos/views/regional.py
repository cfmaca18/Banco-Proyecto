from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.regional import *


class RegionalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Regional.objects.all()
    serializer_class = RegionalSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put