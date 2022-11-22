from django.shortcuts import render
from django.http import JsonResponse
from Api_Proyecto.models import Empleados

# Create your views here.

def verempleados(request):
    emp = {
        'id' : 123,
        'nombre': 'Pedro',
        'email' : 'pedro@inacap.cl',
        'sueldo': '200000000'
    }
    return JsonResponse(emp)

def verempleadosDB(request):
    emple = Empleados.objects.all()
    data = {'empleado': list(emple.values('nombre', 'sueldo'))}
    return JsonResponse(data)