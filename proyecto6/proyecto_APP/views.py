from django.shortcuts import render
from proyecto_APP.forms import FormProyecto #importando FORMS
from proyecto_APP.models import Proyecto

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listaproyectos(request):
    proyecto = Proyecto.objects.all()
    data = {'proyecto': proyecto}
    return render(request, 'proyectos.html', data)

def agreproyecto(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregar.html', data)