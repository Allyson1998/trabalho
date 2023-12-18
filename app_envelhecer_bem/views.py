from django.shortcuts import render

def home(request):
    return render(request, 'usuarios/home.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def login(request):
    return render(request, 'usuarios/login.html')

def menu(request):
  return render(request, 'usuarios/menu.html')