from rest_framework import serializers
from proyectos.models import Programa

class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programa
        fields = ['url', 'nombre']

