
from datetime import datetime
from django.shortcuts import render, HttpResponse 
from PrimerApp.models import Familiar_cercano
from datetime import datetime


def lista(request):
    'función que lista los familiares'
    
    informacion = Familiar_cercano.objects.all
    return render(request, "lista.html", {"Familiar_cercano":informacion})   

def home(request):
    return render(request, "home.html")   

def agregar(request, nombre, apellido, edad, año_nacimiento):
    'función que permite agregar nuevos familiares'
    persona = Familiar_cercano(nombre = nombre, apellido=apellido, edad=edad, año_nacimiento=año_nacimiento, fecha_registro = datetime.now())
    persona.save()
    return render(request, "agregar.html")   

def agregar_main(request):
    return HttpResponse(f"pasar parametros: nombre\apellido\edad\año_nacimiento")