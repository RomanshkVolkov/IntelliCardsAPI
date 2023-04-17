from rest_framework import serializers
from .models import Abs, Biceps, Hombros, Pecho, Piernas

class AbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abs
        fields = ['nombre', 'descripcion', 'imagen']

class BicepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biceps
        fields = ['nombre', 'descripcion', 'imagen']


class HombrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hombros
        fields = ['nombre', 'descripcion', 'imagen']

class PechoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pecho
        fields = ['nombre', 'descripcion', 'imagen']

class PiernasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piernas
        fields = ['nombre', 'descripcion', 'imagen']