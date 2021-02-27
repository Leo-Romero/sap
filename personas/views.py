from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from personas.forms import PersonaForm
from personas.models import Persona


def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

def nuevaPersona(request):
    if request.method == 'POST':
        formPersona = PersonaForm(request.POST)
        if formPersona.is_valid():
            formPersona.save()
            return redirect('inicio')
    else:
        formPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formPersona': formPersona})


def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formPersona = PersonaForm(request.POST, instance=persona)
        if formPersona.is_valid():
            formPersona.save()
            return redirect('inicio')
    else:
        formPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formPersona': formPersona})


def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('inicio')

