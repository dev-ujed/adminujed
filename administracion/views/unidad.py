from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'GET':
        print('holi')
        return render(request, 'admin/unidad/index.html')