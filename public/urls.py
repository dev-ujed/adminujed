from django.urls import path, include
from . import views



urlpatterns = [
	path('', views.index, name='index' ),
	path('login/', views.custom_login, name='login' ),
	path('logout/', views.custom_logout, name='custom_logout' ),
]