from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Radiko, Propono
from .forms import RadikoFormularo, ProponoFormularo


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
# TODO : Paĝo por kontrolistoj ; Radikoj kiuj havas multajn plendojn aperas unue
def radikforigo(request, URLeraro):
    radiko = get_object_or_404(Radiko, eraro=URLeraro)
    radiko.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('ĉefpaĝURLo')


def proponaldono(request, URLeraro):
    radiko = get_object_or_404(Radiko, eraro=URLeraro)
    if request.method == "POST":
        formularo = ProponoFormularo(request.POST)
        if formularo.is_valid():
            propono = formularo.save(commit=False)
            propono.por = radiko
            # TODO : Postaj aferoj
            propono.save()
            return redirect('radikpaĝURLo', URLeraro=radiko.eraro)
    else:
        formularo = ProponoFormularo()
    return render(request, 'vortaro/proponaldonpaĝo.html', {'formularo': formularo})


def proponforigo(request, radikURLeraro, proponURLeraro):
    propono = get_object_or_404(Propono, eraro=proponURLeraro)
    radiko_eraro = propono.por.eraro # Por konservi la eraro-n post la forigo
    propono.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('radikpaĝURLo', URLeraro=radiko_eraro)


# TODO : Kontroli ĉu la uzanto jam voĉdonis
def radikporo(request, radikURLeraro):
    radiko = get_object_or_404(Radiko, eraro=radikURLeraro)
    radiko.poroj = radiko.poroj + 1
    radiko.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('radikpaĝURLo', URLeraro=radiko_eraro)