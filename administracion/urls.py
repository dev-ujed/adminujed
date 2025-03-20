from django.urls import path, include
from  administracion import views

urlpatterns = [
	path('', views.home, name='home' ),
]