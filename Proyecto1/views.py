
from django.http import HttpResponse
from django.template import Template, Context
import datetime 


def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documento = f"Hoy es : {dia}"
    return HttpResponse(documento)

def minombrees(self,nombre):
    documento = f"Mi nombre es: {nombre}"
    
    return HttpResponse(documento)



def inicio(request):
    return HttpResponse("Página de Inicio")

def asistentes(request):
    return HttpResponse("Aca registramos los Asistentes")


def microfonistas(request):
    return HttpResponse("Aca registramos los Microfonistas")


def camarografos(request):
    return HttpResponse("Aca registramos los Camarógrafos")


def probandotemplate(self):
    miHtml = open (r"C:\Users\danie\Escritorio\Pythonproyecto1\Proyecto1\plantillas\template1.html")
    plantilla = Template(miHtml.read())
    micontexto = Context()
    documento = plantilla.render(micontexto)
    return HttpResponse(documento)


