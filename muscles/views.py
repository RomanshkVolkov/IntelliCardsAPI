from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Muscle
from .serializers import MuscleSerializer
from Levenshtein import distance
from django.db.models import Q
from functools import reduce
from operator import or_
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