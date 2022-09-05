from django.http import HttpResponse
import datetime

docu="""<html>
        <body>
            <h1>Hola Alumnos de Django vespertino!!!!</h1>
        </body>
        </html>"""

def saludo(request):
    return HttpResponse(docu)

def chaoo(request):
    return HttpResponse("Hasta la vista Bei Be!!!!")

def hora(request):
    fecha_actual = datetime.datetime.now()
    return HttpResponse("""<html>
                            <body>
                                <h1>Fecha y Hora actuales %s</h1>
                            </body>
                            </html>"""%fecha_actual)

def calculaedad(request,agno.):
    edadactual=18
    periodo = agno - 2022
    edadfutura = edadactual + periodo
    return HttpResponse("""<html>
                            <body>
                                <h1>En el año %s tendras %s años</h1>
                            </body>
                            </html>"""%(agno, edadfutura))