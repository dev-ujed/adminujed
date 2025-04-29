from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from administracion.models import Profesor_grupo, Oparametros_dtd, Escuelas, Usuarios, Grupo, Plan_materia, Materias
from .unidad import ciclos_anteriores

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

def detalles_profesor(request, matricula, ciclo=None):
    profesor =  Profesor_grupo.objects.filter(pl_matricula=matricula).first()
    usuario = Usuarios.objects.filter(matricula=matricula).first()
    ciclo_actual = Oparametros_dtd.objects.get(id=61).valor

    if ciclo is None:
        ciclo = ciclo_actual

    if not usuario:
        return JsonResponse({'error': 'La matricula no esta en la tabla de usuarios'}, status=404)

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

        info_materias = detalles_materias(matricula, ciclo)
        ciclos = ciclos_anteriores()


    return render(request, 'admin/profesor/detalles.html', {'profesor': profesor_data, 'info_materias': info_materias, 'ciclos': ciclos})

def detalles_materias(matricula, ciclo):

    #ciclo_actual = Oparametros_dtd.objects.get(id=61).valor

    grupos = Grupo.objects.filter(cve_maestro=matricula, cve_ciclo=ciclo).values('cve_grupo', 'cve_materia', 'cve_carrera', 'cve_escuela', 'plan_estudio_id', 'cve_plan')
    claves_materias = [
        {
            'cve_materia': g['cve_materia'],
            'plan_estudio_id':g['plan_estudio_id']
        }
        for g in grupos
    ]

    cve_materias = [cm['cve_materia'] for cm in claves_materias]
    plan_ids = [cm['plan_estudio_id'] for cm in claves_materias]
    claves_escuelas = list(set(g['cve_escuela'] for g in grupos))
    escuelas = Escuelas.objects.filter(cve_escuela__in=claves_escuelas).values('cve_escuela', 'desc_escuela', 'desc_corto')
    escuelas_dict = {e['cve_escuela']: e['desc_escuela'] for e in escuelas}
    escuelas_nom_corto = {e['cve_escuela']: e['desc_corto'] for e in escuelas}

    plan_materias = Plan_materia.objects.filter(cve_materia__in=cve_materias, plan_estudio_id__in=plan_ids).values('cve_materia', 'horas_semana', 'virtual')
    materias = Materias.objects.filter(cve_materia__in=cve_materias).values('cve_materia', 'desc_corto')

    plan_materias_dict = {pm['cve_materia']: pm for pm in plan_materias}
    materias_dict = {m['cve_materia']: m for m in materias}

    resultados = []
    for grupo in grupos:
        cve_materia = grupo['cve_materia']
        cve_carrera = grupo['cve_carrera']
        cve_escuela = grupo['cve_escuela']
        cve_plan = grupo['cve_plan']
        nombre_escuela = escuelas_dict.get(cve_escuela, 'NA')
        nombre_corto = escuelas_nom_corto.get(cve_escuela, 'NA')
        plan = plan_materias_dict.get(cve_materia)
        materia = materias_dict.get(cve_materia)

        if plan and materia:
            modalidad = (
                'Virtual' if plan['virtual'] == 'S'
                else 'Presencial' if plan['virtual'] == 'N'
                else 'Otra modalidad'
            )

            nivel = obtener_nivel(cve_carrera)

            resultados.append({
                'profesor': matricula,
                'grupo': grupo['cve_grupo'],
                'cve_materia': cve_materia,
                'cve_carrera': cve_carrera,
                'cve_plan': cve_plan,
                'nivel': nivel,
                'cve_escuela': cve_escuela,
                'nombre_escuela': nombre_escuela,
                'nombre_escuela_corto': nombre_corto,
                'materia': materia['desc_corto'],
                'horas_semanas': plan['horas_semana'],
                'modalidad': modalidad
            })
    
    return resultados

def detalles_materias_ciclo(request, matricula, cve_ciclo):

    response_data = list(detalles_materias(matricula, cve_ciclo))

    return JsonResponse(response_data, safe=False)

def obtener_nivel(cve_carrera):
    try:
        clave = int(cve_carrera)
        if 140000 <= clave <= 149999:
            return 'LICENCIATURA'
        elif 160000 <= clave <= 169999:
            return 'MAESTRÍA'
        elif 170000 <= clave <= 179999:
            return 'DOCTORADO'
        elif 12000201 <= clave <= 12000206:
            return 'PREPARATORIA'
        else:
            return 'OTRO'
    except:
        return 'NA'