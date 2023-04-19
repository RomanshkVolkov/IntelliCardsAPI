from django.urls import path
from .views import MuscleList, MuscleSuggestionView, MuscleSuggestionIntelliView, FolderListCreateView, CreateUserView

urlpatterns = [
    path('', MuscleList.as_view(), name='muscle-list'),
    path('suggest/', MuscleSuggestionView.as_view(), name='muscle-suggestion'),
    path('suggest_intelli/', MuscleSuggestionIntelliView.as_view(), name='muscle-suggestion-intelli'),
    path('folders/', FolderListCreateView.as_view(), name='folder-list-create'),
    path('user/folder/', CreateUserView.as_view(), name='user-folder-create'),
]
