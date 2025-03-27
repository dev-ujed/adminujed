from django.urls import path, include
from  administracion.views import views, unidad, profesor

urlpatterns = [
	path('', views.home, name='home' ),
	path('unidad/', unidad.index, name='unidad' ),
	path('unidad/<int:id>/', unidad.detalles_unidad, name='detalles_unidad'),
	path('profesor/', profesor.index, name='profesor' ),
]