from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('clubs/', views.club_list, name='club-list'),
    path('music_list/', views.music_list, name='music-list'),
]
