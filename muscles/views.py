from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Muscle, Folder, CustomUser
from .serializers import MuscleSerializer, FolderSerializer, CustomUserSerializer
from django.db.models import Value
from django.db.models.functions import Concat
from djongo import models as djongo_models
from unidecode import unidecode


class MuscleList(APIView):
    def get(self, request):
        muscles = Muscle.objects.all()
        serializer = MuscleSerializer(muscles, many=True)
        return Response(serializer.data)


class MuscleSuggestionView(generics.ListAPIView):
    serializer_class = MuscleSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            search = unidecode(search)
            return Muscle.objects.filter(name__icontains=search)[:10]
        else:
            return Muscle.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class MuscleSuggestionIntelliView(generics.ListAPIView):
    serializer_class = MuscleSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            search_query = djongo_models.TextSearch(search, config='simple')
            search_rank = djongo_models.TextRank(search_query)
            search_vectors = djongo_models.SearchVector(Concat('name', Value(' ')))

            return Muscle.objects.annotate(rank=search_rank(search_vectors)).filter(rank__gte=0.1).order_by('-rank')[:10]
        else:
            return Muscle.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class FolderListCreateView(generics.ListCreateAPIView):
    serializer_class = FolderSerializer

    def get_queryset(self):
        user_email = self.request.query_params.get('email', None)
        if user_email is not None:
            user = CustomUser.objects.get(email=user_email)
            return Folder.objects.filter(user=user)
        return Folder.objects.none()
    
class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        # Crear carpeta predeterminada y asociarla al usuario creado
        default_folder = Folder(name='Default')
        default_folder.save()
        user.folders.add(default_folder)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()