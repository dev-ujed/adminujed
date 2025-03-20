from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'GET':
        print('holi')
        site = request.scheme+'://'+request.get_host()

        return render(request, 'admin/profesor/index.html', {'SITE_URL':site})