from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as logins, logout as logouts, authenticate
from django.db import IntegrityError
# Create your views here.


def home(request):
    return render(request, 'home.html', {'title': 'Inicio'})


def register(request):
    # return HttpResponse("<h1>Pagina de Registro</h1>")
    print(request.method, request.path, request.user)
    if request.method == 'GET':
        print(request.GET)
        context = {'title': 'Registro de usuario', 'form': UserCreationForm()}
        # return render(request,'register/register.html',{'title':'Usuario'})
        return render(request, 'register/register.html', context)
    else:
        print(request.POST)  # ={"username":"erick","password1":"123"}
        print(request.POST['username'])
        # return redirect('home')
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                # insert into User (username,password) values('erick','123')
                user.save()  # graba en la BD
                # return JsonResponse({'msg':'!!! Usuario grabado sastifactoriamente!!!'})
                # logins(request,user) # crea una cooki del usuario registrado
                return redirect('home')
            except:
                context = {'title': 'Registro de Usuario', 'form': UserCreationForm(
                    request.POST), 'error': 'Usuario ya existe'}
                return render(request, 'register/register.html', context)
        # return HttpResponse('<h2>!!!Password no coinciden!!!</h2>')data=request.POST
        context = {'title': 'Registro de Usuario', 'form': UserCreationForm(
            request.POST), 'error': 'Password no coinciden'}
        return render(request, 'register/register.html', context)


def login(request):
    return render(request, 'register/login.html', {'title': 'Sesion'})


def logout(request):
    return redirect('home')


def student(request):
    return render(request, 'students/student.html', {'title': 'Estudiantes'})
