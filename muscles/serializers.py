from rest_framework import serializers
from .models import Muscle, Folder, CustomUser

class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = '__all__'

class FolderSerializer(serializers.ModelSerializer):
    muscles = MuscleSerializer(many=True, read_only=True)
    class Meta:
        model = Folder
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    folders = FolderSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = '__all__'
