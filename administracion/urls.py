from django.urls import path, include
from  administracion.views import views, unidad, profesor

urlpatterns = [
	path('', views.home, name='home' ),
	path('unidad/', unidad.index, name='unidad' ),
	path('unidad/unidades/', unidad.unidades, name='unidades'),
	path('carreras/<str:cve_escuela>/', unidad.carreras, name="carreras"),
	path('profesor/', profesor.index, name='profesor' ),
	 path('profesor/info/', profesor.infoProfesor, name='profesor_info'),
]