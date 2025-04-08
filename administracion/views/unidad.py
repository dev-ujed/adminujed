from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count, F

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
    planes_con_nombre = Plan_estudio.objects.filter(cve_plan__in=planes_actual).values('cve_plan', 'desc_plan')
    
    planes_actuales_dic = list(planes_con_nombre)

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
    
    #print(materias_por_semestre)

    return JsonResponse(materias_por_semestre, safe=False)

def info_materias(request):

    ciclo_actual = Oparametros_dtd.objects.get(id=61).valor
    cve_carrera = request.GET.get('carrera')
    cve_plan = request.GET.get('plan')
    cve_materia = request.GET.get('cve_materia')


    #INFORMACIÓN DE LA MATERIA
    resultado_cadena = []
    
    plan_materia_base = Plan_materia.objects.filter(cve_plan=cve_plan, cve_materia=cve_materia).first()

    if plan_materia_base:
        materias_relacionadas = Materias_cadenas.objects.filter(cve_materia=cve_materia).values('cadena_padre')
        materias_encadenadas = {cadena['cadena_padre'] for cadena in materias_relacionadas}

        materia = Materias.objects.get(cve_materia=plan_materia_base.cve_materia)
        
        nombres_materias_encadenadas = []
        for cve_materia in materias_encadenadas:
            materia_encadenada = Materias.objects.get(cve_materia=cve_materia)
            nombres_materias_encadenadas.append(materia_encadenada.desc_materia)
    
        resultado_cadena.append({
            'materia': materia.desc_materia,
            'clave': plan_materia_base.cve_materia,
            'horas': plan_materia_base.horas_semana,
            'creditos': plan_materia_base.creditos,
            'materias_encadenadas': ', '.join(sorted(set(nombres_materias_encadenadas))),
        })
    
    # ESTA ES INFORMACIÓN DE LOS GRUPOS Y MAESTROS DE ESA MATERIA DEL CICLO ACTUAL
    grupos_info = []

    grupos = Grupo.objects.filter(cve_carrera=cve_carrera, cve_ciclo=ciclo_actual, cve_materia=cve_materia)
    inscritos_por_grupo = (
        Materia_alumno.objects.filter(cve_grupo__in=grupos, cve_ciclo=ciclo_actual, cve_plan=cve_plan, cve_materia=cve_materia)
        .values('cve_grupo')
        .annotate(inscritos=Count('cve_alumno', distinct=True))
    )

    inscritos_dict = {item['cve_grupo']: item['inscritos'] for item in inscritos_por_grupo}

    
    for grupo in grupos:

        nombre_maestro = Profesor_grupo.objects.filter(pl_matricula=grupo.cve_maestro).values_list('nom', flat=True).first() or 'Sin asignar'
        grupos_info.append({
            'grupo': grupo.cve_grupo,
            'materia': grupo.cve_materia,
            'maestro': grupo.cve_maestro,
            'nom_maestro': nombre_maestro,
            'cupo': grupo.cupo,
            'inscritos': inscritos_dict.get(grupo.cve_grupo, 0),
        })

    ciclos = ciclos_anteriores()

    return JsonResponse({ 'grupos': grupos_info, 'info_materia': resultado_cadena, 'ciclos': ciclos }, safe=False)

def grupos_por_ciclo(request, cve_ciclo, cve_carrera, cve_materia, cve_plan):
    grupos_info = []

    grupos = Grupo.objects.filter(cve_carrera=cve_carrera, cve_ciclo=cve_ciclo, cve_materia=cve_materia)
    inscritos_por_grupo = (
        Materia_alumno.objects.filter(cve_grupo__in=grupos, cve_ciclo=cve_ciclo, cve_plan=cve_plan, cve_materia=cve_materia)
        .values('cve_grupo')
        .annotate(inscritos=Count('cve_alumno', distinct=True))
    )

    inscritos_dict = {item['cve_grupo']: item['inscritos'] for item in inscritos_por_grupo}

    
    for grupo in grupos:

        nombre_maestro = Profesor_grupo.objects.filter(pl_matricula=grupo.cve_maestro).values_list('nom', flat=True).first() or 'Sin asignar'
        grupos_info.append({
            'grupo': grupo.cve_grupo,
            'materia': grupo.cve_materia,
            'maestro': grupo.cve_maestro,
            'nom_maestro': nombre_maestro,
            'cupo': grupo.cupo,
            'inscritos': inscritos_dict.get(grupo.cve_grupo, 0),
        })

    print(grupos_info)
    
    return JsonResponse({ 'grupos': grupos_info }, safe=False)

def ciclos_anteriores():

    ciclo_actual = Oparametros_dtd.objects.get(id=61).valor

    ciclos = (
        Ciclos.objects
        .filter(cve_ciclo__lte=ciclo_actual)
        .order_by('-f_final')
    )

    ciclos_filtrados = [c for c in ciclos if c.cve_ciclo % 5 == 0][:4]

    ciclos_json = [{'cve_ciclo': c.cve_ciclo, 'desc_ciclo': c.desc_ciclo} for c in ciclos_filtrados]

    print("Ciclos obtenidos desde la base de datos:", ciclos_json)

    return ciclos_json
    #return render(request, "admin/unidad/programa.html", {'ciclos': ciclos_json})