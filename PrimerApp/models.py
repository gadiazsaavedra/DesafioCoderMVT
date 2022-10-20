from enum import auto
from django.db import models

# Create your models here.

class Familiar_cercano(models.Model):
    nombre = models.CharField(max_length = 25)
    apellido  = models.CharField(max_length = 25)
    edad = models.IntegerField()
    año_nacimiento =  models.IntegerField()
    fecha_registro = models.DateField(auto_now = True)


