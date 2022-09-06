import datetime
from django.http import HttpResponse
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def plantilla(request): # Primera Vista

    #nombre = "Pedro"   #usando parametros
    #apellido = "Gaete"

    ahora = datetime.datetime.now() #trae fecha de ahora

    p1 = Persona("Profesor Pedro", "Gaete")

    doc_externo = open("D:/1. Clases INACAP/2. Clases/2.31 Programacion Back-End/Proyectos-AP-77/Proyecto_AP_77/proyecto2/Proyecto2/web/miplantilla.html")

    plantilla = Template(doc_externo.read())

    doc_externo.close()

    context = Context({"nom_persona":p1.nombre, "apel_persona":p1.apellido, "fecha":ahora})

    documento = plantilla.render(context)
    
    return HttpResponse(documento)