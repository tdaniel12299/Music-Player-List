from django.urls import path
from . import views
from . import (
    MusicCreateView,
    MusicDeleteView,
    MusicListView,
    MusicDetailView,
)

urlpatterns = [
    path('',MusicListView.as_view(), name="music-list"),
    path('search',views.search, name="search"),
    path('create',MusicCreateView.as_view(),name="music-create"),
    path('music_details/<int:pk>/',MusicDetailView.as_view(),name="music-details"),
    path('update/<int:pk>/',views.music_update,name="music-update"),
    path('delete/<int:pk>/',MusicDeleteView.as_view(),name="music-delete"),

]