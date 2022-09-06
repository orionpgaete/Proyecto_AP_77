import datetime
from django.http import HttpResponse
from django.template import Template, Context

def plantilla(request): # Primera Vista

    nombre = "Pedro"   #usando parametros
    apellido = "Gaete"

    ahora = datetime.datetime.now() #trae fecha de ahora

    doc_externo = open("D:/1. Clases INACAP/2. Clases/2.31 Programacion Back-End/Proyectos-AP-77/Proyecto_AP_77/proyecto2/Proyecto2/web/miplantilla.html")

    plantilla = Template(doc_externo.read())

    doc_externo.close()

    context = Context({"nom_persona":nombre, "apel_persona":apellido, "fecha":ahora})

    documento = plantilla.render(context)
    
    return HttpResponse(documento)