from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from administracion.models import *

# Create your views here.

def index(request):
    if request.method == 'GET':
        site = request.scheme+'://'+request.get_host()
        
        return render(request, 'admin/unidad/index.html', {'SITE_URL':site})


def unidades(request):
    #escuelas = Escuelas.objects.all().values("cve_escuela", "desc_completo", "desc_corto", "ubicacion")
    #gte (mayor o igual) y lte (menor o igual)

    licenciaturas = Carreras.objects.filter(cve_carrera__gte="140000", cve_carrera__lte="149999")
    maestrias = Carreras.objects.filter(cve_carrera__gte="160000", cve_carrera__lte="169999")
    doctorados = Carreras.objects.filter(cve_carrera__gte="170000", cve_carrera__lte="179999")
    prepas = Carreras.objects.filter(cve_carrera__gte="12000201", cve_carrera__lte="12000206")

    escuelas = Escuelas.objects.filter(
        cve_escuela__in=licenciaturas.values('cve_escuela') |
        maestrias.values('cve_escuela') |
        doctorados.values('cve_escuela') |
        prepas.values('cve_escuela')
    ).values("cve_escuela", "desc_completo", "desc_corto", "ubicacion").distinct()

    return JsonResponse(list(escuelas), safe=False)

def carreras(request, cve_escuela):

    carreras = Carreras.objects.filter(cve_escuela=cve_escuela).distinct()
    planes = Plan_estudio.objects.filter(cve_carrera__in=carreras.values_list('cve_carrera', flat=True))

    planes_dict = {}
    for plan in planes:
        if plan.cve_carrera not in planes_dict or plan.cve_ciclo > planes_dict[plan.cve_carrera]['cve_ciclo']:
            planes_dict[plan.cve_carrera] = {'anio': plan.anio, 'cve_ciclo': plan.cve_ciclo}

    #carreras_data = list(carreras.values('cve_carrera', 'desc_carrera', 'cve_escuela', 'activa'))
    
    carreras_data = []
    for carrera in carreras:
        anio = planes_dict.get(carrera.cve_carrera, {}).get('anio', None)
        carreras_data.append({
            'cve_carrera': carrera.cve_carrera,
            'desc_carrera': carrera.desc_carrera,
            'cve_escuela': str(carrera.cve_escuela),
            'activa': carrera.activa,
            'anio': anio
        })

    return render(request, 'admin/unidad/detalles.html', {'carreras': carreras_data})

def programa(request, cve_carrera):

    planes_actual = Ciclo_carrera.objects.filter(cve_carrera=cve_carrera, estatus_ciclo='A').values('cve_plan')
    
    planes_actuales_dic = list(planes_actual)

    return render(request, "admin/unidad/programa.html", {'cve_carrera': cve_carrera, 'planes_actuales': planes_actuales_dic})


def materias_plan_actual(request):

    cve_plan = request.GET.get('cve_plan')

    if not cve_plan:
        return JsonResponse({"error": "Falta el parámetro cve_plan"}, status=400)

    materias = Plan_materia.objects.filter(cve_plan=cve_plan).values('cve_materia', 'semestre')

    materias_por_semestre = {}

    for materia in materias:
        nombre_materia = Materias.objects.filter(cve_materia=materia['cve_materia']).values('desc_materia').first()

        if nombre_materia:
            if materia['semestre'] not in materias_por_semestre:
                materias_por_semestre[materia['semestre']] = []
            
            materias_por_semestre[materia['semestre']].append({
                'cve_materia': materia['cve_materia'],
                'desc_materia': nombre_materia['desc_materia'],
                'semestre': materia['semestre']
            })
    
    print(materias_por_semestre)

    return JsonResponse(materias_por_semestre, safe=False)
