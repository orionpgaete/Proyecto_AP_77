from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def busqueda(request):
    return render(request, "busqueda_producto.html")

def buscar(request):
    if request.GET ["prd"]:
        mensaje = "Articulo buscado: %r" %request.GET["prd"]
    else:
        mensaje="No has introducido nada"
        
    return HttpResponse(mensaje)