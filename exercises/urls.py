from django.urls import path
from .views import AbsListView, BicepsListView, HombrosListView, PechoListView, PiernasListView

urlpatterns = [
    path('abs/', AbsListView.as_view(), name='abs_list'),
    path('biceps/', BicepsListView.as_view(), name='biceps_list'),
    path('hombros/', HombrosListView.as_view(), name='hombros_list'),
    path('pecho/', PechoListView.as_view(), name='pecho_list'),
    path('piernas/', PiernasListView.as_view(), name='piernas_list'),
]
