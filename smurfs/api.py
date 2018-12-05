from rest_framework import serializers, viewsets
from .models import Smurf

class SmurfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Smurf
        fields = ('id', 'name', 'age', 'height')

    def create(self, validated_data):
        smurf = Smurf.objects.create(**validated_data)
        return smurf

class SmurfViewSet(viewsets.ModelViewSet):
    serializer_class = SmurfSerializer
    queryset = Smurf.objects.all()