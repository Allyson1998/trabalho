from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('main_menu/', views.main_menu, name='main_menu'),
    path('consulta/', views.consulta, name='consulta'),

]