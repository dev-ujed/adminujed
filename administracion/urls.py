from django.urls import path, include
from  administracion.views import views, unidad, profesor

urlpatterns = [
	path('', views.home, name='home' ),
	path('unidad/', unidad.index, name='unidad' ),
	path('unidad/unidades/', unidad.unidades, name='unidades'),
	path('programa/<str:cve_carrera>/', unidad.programa, name='programa'),
	path('carreras/<str:cve_escuela>/', unidad.carreras, name="carreras"),
	path('materias_plan/', unidad.materias_plan_actual, name="materias_plan"),
	path('materia-info/', unidad.info_materias, name="materia-info"),
    path('grupos-ciclos/<int:cve_ciclo>/<str:cve_carrera>/<str:cve_materia>/<str:cve_plan>', unidad.grupos_por_ciclo, name='grupos_por_ciclo'),

	path('profesor/', profesor.index, name='profesor' ),
	path('profesor/info/', profesor.infoProfesor, name='profesor_info'),
    path('profesor/<str:matricula>/', profesor.detalles_profesor, name='detalles_profesor'),
]