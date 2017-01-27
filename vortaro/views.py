from django.shortcuts import render, get_object_or_404, redirect
from .models import Radiko
from .forms import RadikoFormularo


# Create your views here.
def ĉefpaĝo(request):
    radikoaro = Radiko.objects.order_by('malporoj') # Xoaro = array de Xo
    return render(request, 'vortaro/ĉefpaĝo.html', {'radikoaro': radikoaro})


def radikpaĝo(request, URLeraro):
    radiko = get_object_or_404(Radiko, eraro=URLeraro)
    return render(request, 'vortaro/radikpaĝo.html', {'radiko': radiko})


def aldonpaĝo(request):
    # Se la formularo estas konservita
    if request.method == "POST":
        formularo = RadikoFormularo(request.POST)
        if formularo.is_valid():
            radiko = formularo.save(commit=False)
            # TODO : Eble poste formularo.aŭtoro = request.user
            radiko.save()
            return redirect('radikpaĝURLo', URLeraro=radiko.eraro)
    # Se la formularo estas nova (paĝo ĵus vizitita)
    else:
        formularo = RadikoFormularo()
    return render(request, 'vortaro/aldonpaĝo.html', {'formularo': formularo})


# TODO : @NurPorKontrolantoj
# TODO : Paĝo por kontrolantoj ; Radikoj kiuj havas multajn plendojn aperas unue
def forigo(request, URLeraro):
    radiko = get_object_or_404(Radiko, eraro=URLeraro)
    radiko.delete()
    return redirect('ĉefpaĝURLo')