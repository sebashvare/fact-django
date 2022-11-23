from django.shortcuts import render
# Esta clase me permite ejecutar una respestuesta Http
from django.http import HttpResponse

# Creacion de las vistas.

def index(request):
    return HttpResponse("Hola Sebastian")

