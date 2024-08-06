

from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
 


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
    
    dia = datetime.now()
    nombre = "Daniel"
    apellido = "Yauny"
    listadenotas = 2,2,3,7,2,5
    diccionario = {"nomb":nombre, "ape":apellido, "dia": dia, "lista": listadenotas}
    miHtml = open (r"C:\Users\danie\Escritorio\Pythonproyecto1\Proyecto1\plantillas\template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    micontexto = Context(diccionario)
    documento = plantilla.render(micontexto)
    return HttpResponse(documento)



def probandocargadores(request):
    
    nombre = "Daniel"
    apellido = "Yauny"
    
    context = {"nomb": nombre, "ape": apellido}
    
    plantilla = loader.get_template("template2.html")
    
    documento = plantilla.render(context)
    
    return HttpResponse(documento)
    
    
    


