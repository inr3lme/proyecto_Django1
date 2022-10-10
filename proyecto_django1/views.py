from contextvars import Context
from django.http import HttpResponse

from datetime import datetime

from django.template import Context, Template

def hola(request):
    return HttpResponse('Tamplate de Laura')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La fecha actual es {fecha_actual}')

# def mi_template(request):
#     return HttpResponse('esto no es un template')

# Ahora usando html
def mi_template(request):
    cargar_archivo = open(r'C:\Users\edelmanl\Documents\ProyectosPython\Clase_17_Django_Porfolio_Parte1\proyecto_Django1\templates\template.html','r')
   
    el_template_es = Template(cargar_archivo.read())
    
    cargar_archivo.close()

    contexto = Context()
    
    el_template_renderizado_es = el_template_es.render(contexto)
    
    return HttpResponse(el_template_renderizado_es)    
     