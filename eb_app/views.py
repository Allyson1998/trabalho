from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def home(request):
        return render(request, 'home.html')
    
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return render(request, 'erro_cadastro.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return render(request, 'login.html')   

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            return render(request, "main_menu.html")
        else: 
            return render(request, "erro_login.html")

def main_menu(request):
        return render(request, 'main_menu.html')
def consulta(request):
        return render(request, 'consulta.html')
def validacao(request):
        return render(request, 'validacao.html')
def conta(request):
        return render(request, 'conta.html')
def medicamentos(request):
        return render(request, 'medicamentos.html')