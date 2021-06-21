from django.shortcuts import render
from clases.models import Clase

# Create your views here.
def get_clases(request):
    clases = Clase.objects.all()
    context = {
        'clases': clases
    }
    return render(request, 'clases/clases.html', context)