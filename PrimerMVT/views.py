
from django.shortcuts import render, HttpResponse 
from PrimerApp.models import Familiar_cercano

def saludo(request):
 
    informacion = Familiar_cercano.objects.all
    return render(request, "index.html", {"Familiar_cercano":informacion})   

