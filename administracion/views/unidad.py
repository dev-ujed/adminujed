from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'GET':
        print('holi')
        site = request.scheme+'://'+request.get_host()
        
        return render(request, 'admin/unidad/index.html', {'SITE_URL':site})

def detalles_unidad(request, id):
    #todavía no tengo modelo de eso para sacar las unidades usare este de ejemplo
    unidades = {
        1: {"nombre_corto": "CCH", "nombre_largo": "Colegio de ciencias y humanidades", "sede":"Sede en Durango"},
        2: {"nombre_corto": "ECT", "nombre_largo": "Escuela de Ciencias y Tecnologías", "sede":"Sede en Durango"},
        3: {"nombre_corto": "FCQ", "nombre_largo": "Facultad de Ciencias Químicas", "sede":"Sede en Durango"},
    }

    unidad = unidades.get(id, None)

    if not unidad:
        return "sin unidad"

    return render(request, 'admin/unidad/detalles.html', {'unidad': unidad})
        
        