from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import *
from .serializers import *
import json
from django.contrib.auth.decorators import login_required


def index(request):
	if request.method == 'GET':
		if request.user.is_authenticated:
			print('logueado')
		return render(request, 'public/index.html')
    
def custom_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login exitoso', 'user': customUserSerializer(user).data}, status=200)
        else:
            return JsonResponse({'error': 'Correo o contraseña incorrectos.'}, status=401)

def custom_logout(request):
    logout(request)
    return redirect('/')

def create_user(request):
	if request.method == 'POST':
		data 			= json.loads(request.body)
		email 			= data.get('email')
		password 		= data.get('password')
		matricula 		= data.get('matricula')
		name 			= data.get('name')
		last_name 		= data.get('last_name')

		user = CustomUser(
			email=email,
			name=name,
			password=make_password(password),
			matricula=matricula,
			last_name=last_name
		)
		user.save()
  
		return JsonResponse({'message': 'Login exitoso'}, status=200)