from django.http import HttpResponse
from django.shortcuts import render
from personas.models import Persona


def bienvenido(request):
    num_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenida.html', {'cantidad': num_personas, 'personas': personas})
