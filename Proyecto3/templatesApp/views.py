from django.shortcuts import render

# Create your views here.
def miplantilla(request):
    data = {"nombre" : "Pedro", "apellido": "Gaete"}
    return render(request, 'templateweb/miplantilla.html', data)