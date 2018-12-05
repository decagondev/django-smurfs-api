from rest_framework import serializers, viewsets
from .models import Smurf

class SmurfSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Smurf
        fields = ('name', 'age', 'height')

class SmurfViewSet(viewsets.ModelViewSet):
    serializer_class = SmurfSerializer
    queryset = Smurf.objects.all()