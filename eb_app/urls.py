from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('consulta/', views.consulta, name='consulta'),
    path('validacao/', views.validacao, name='validacao'),
    path('conta/', views.conta, name='conta'),
]