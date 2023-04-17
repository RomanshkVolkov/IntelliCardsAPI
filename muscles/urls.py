from django.urls import path
from .views import MuscleList, MuscleSuggestionView, MuscleSuggestionIntelliView

urlpatterns = [
    path('', MuscleList.as_view(), name='muscle-list'),
    path('suggest/', MuscleSuggestionView.as_view(), name='muscle-suggestion'),
    path('suggest_intelli/', MuscleSuggestionIntelliView.as_view(), name='muscle-suggestion-intelli'),
]
