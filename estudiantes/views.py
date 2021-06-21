from django.http.response import HttpResponse
from django.shortcuts import render
from estudiantes.models import Estudiante
from clases.models import Clase

# Create your views here.
def home(request):
    return HttpResponse("Bienvenido")

def get_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    context = {
        'estudiantes': estudiantes
    }
    return render(request, 'estudiantes/estudiantes.html', context)

def get_estudiante(request, estudiante_id):
    try:
        estudiante = Estudiante.objects.get(id=estudiante_id)
        context = {
            'estudiante': estudiante,
        }
        return render(request, 'estudiantes/estudiante_detalle.html', context)
    except:
        return render(request, 'estudiantes/estudiante_detalle.html', {})