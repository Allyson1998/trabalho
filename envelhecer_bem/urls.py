from django.urls import path
from app_envelhecer_bem import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    # envelhecerbem.com
    path('', views.home, name='home'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('menu', views.menu, name='menu'),
]
