from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def verempleados(request):
    emp = {
        'id' : 123,
        'nombre': 'Pedro',
        'email' : 'pedro@inacap.cl',
        'sueldo': '200000000'
    }
    return JsonResponse(emp)