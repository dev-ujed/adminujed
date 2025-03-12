from django.shortcuts import render
from django.http import HttpResponse
from .models import Omov_alumno

# Create your views here.

def index(request):
	alumno = Omov_alumno.objects.all()
	return render(request, 'public/index.html')