from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('jogo/', views.jogo, name='jogar'),
    path('index/', views.index, name='voltar'),
]
