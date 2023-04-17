from rest_framework import generics
from .models import Abs, Biceps, Hombros, Pecho, Piernas
from .serializers import AbsSerializer, BicepsSerializer, HombrosSerializer, PechoSerializer, PiernasSerializer

class AbsListView(generics.ListAPIView):
    queryset = Abs.objects.all()
    serializer_class = AbsSerializer

class BicepsListView(generics.ListAPIView):
    queryset = Biceps.objects.all()
    serializer_class = BicepsSerializer

class HombrosListView(generics.ListAPIView):
    queryset = Hombros.objects.all()
    serializer_class = HombrosSerializer

class PechoListView(generics.ListAPIView):
    queryset = Pecho.objects.all()
    serializer_class = PechoSerializer

class PiernasListView(generics.ListAPIView):
    queryset = Piernas.objects.all()
    serializer_class = PiernasSerializer
