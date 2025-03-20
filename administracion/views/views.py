from django.shortcuts import render

# Create your views here.

def home(request):
	if request.method == 'GET':
		if request.user.is_authenticated:
			print('logueado')
   
		return render(request, 'admin/home.html', {'SITE_URL':'http://localhost:8000/'})