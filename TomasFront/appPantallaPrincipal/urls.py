from django.urls import path
from . import views

urlpatterns = [
    path('', views.initialView, name='initialView'),
    path('home/', views.homeView, name='homeView'),
    path('talking/', views.talkingView, name='talkingView'),
    path('vision/', views.visionView, name='visionView'),
    path('gameSelect/', views.gameSelectView, name='gameSelectView'),
    path('game/', views.gameView, name='gameView'),
]