from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from administracion.models import Profesor_grupo, Oparametros_dtd, Escuelas, Usuarios

# Create your views here.

def index(request):
    if request.method == 'GET':
        site = request.scheme+'://'+request.get_host()

        return render(request, 'admin/profesor/index.html', {'SITE_URL':site})

def infoProfesor(request):
    if request.method == 'GET':
        ciclo_actual = Oparametros_dtd.objects.get(id=61).valor

        search_query = request.GET.get('search', '').strip().upper()

        profesores = list(Profesor_grupo.objects.values(
            'pl_matricula', 'nom', 'escuela', 'autorizacion', 'pl_ciclo'
        ))

        if search_query:
            profesores = [
                profesor for profesor in profesores
                if search_query in profesor['pl_matricula'] or search_query in profesor['nom']
            ]

        profesores_unicos = {}
        for profesor in profesores:
            if profesor['pl_matricula'] not in profesores_unicos:
                profesores_unicos[profesor['pl_matricula']] = profesor

        for profesor in profesores_unicos.values():
            try:
                escuela = Escuelas.objects.get(cve_escuela=profesor['escuela'])
                profesor['escuela_nombre'] = escuela.desc_completo
            except Escuelas.DoesNotExist:
                profesor['escuela_nombre'] = 'Escuela no encontrada'

        profesores_list = list(profesores_unicos.values())

        total_profes = len(profesores_list)

        #Paginación
        page_number = request.GET.get('page', 1)
        paginator = Paginator(profesores_list, 10)
        page = paginator.get_page(page_number)

        response_data = {
            'profesores': list(page),
            'total_pages': paginator.num_pages,
            'current_page': page.number,
            'total_items': paginator.count,
            'total_results': total_profes
        }

        return JsonResponse(response_data, safe=False)

def detalles_profesor(request, matricula):
    profesor =  Profesor_grupo.objects.filter(pl_matricula=matricula).first()
    usuario = Usuarios.objects.filter(matricula=matricula).first()

    if not usuario:
        return JsonResponse({'error': 'La matrícula no está en la tabla de usuarios'}, status=404)

    if profesor:
        profesor_data = {
            'pl_matricula': profesor.pl_matricula,
            'nom': profesor.nom,
            'escuela': profesor.escuela,
            'autorizacion': profesor.autorizacion,
            'pl_ciclo': profesor.pl_ciclo,
            'correo': usuario.correo,
            'activo': usuario.activo,
        }


    return render(request, 'admin/profesor/detalles.html', {'profesor': profesor_data})