from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Radiko, Propono
from .forms import RadikoFormularo, ProponoFormularo


# Create your views here.
def ĉefpaĝo(request):
    radikoaro = Radiko.objects.order_by('boneco') # pli malboneca (malgranda) unue
    return render(request, 'vortaro/ĉefpaĝo.html', {'radikoaro': radikoaro})


def radikpaĝo(request, radikURLeraro):
    radiko = get_object_or_404(Radiko, eraro=radikURLeraro)
    return render(request, 'vortaro/radikpaĝo.html', {'radiko': radiko})


def aldonpaĝo(request):
    # Se la formularo estas konservita
    if request.method == "POST":
        formularo = RadikoFormularo(request.POST)
        if formularo.is_valid():
            radiko = formularo.save(commit=False)
            # TODO : Eble poste formularo.aŭtoro = request.user
            radiko.save()
            return redirect('radikpaĝURLo', radikURLeraro=radiko.eraro)
    # Se la formularo estas nova (paĝo ĵus vizitita)
    else:
        formularo = RadikoFormularo()
    return render(request, 'vortaro/aldonpaĝo.html', {'formularo': formularo})


# TODO : @NurPorKontrolantoj
# TODO : Paĝo por kontrolistoj ; Radikoj kiuj havas multajn plendojn aperas unue
def radikforigo(request, radikURLeraro):
    radiko = get_object_or_404(Radiko, eraro=radikURLeraro)
    radiko.delete()
    # TODO : Ĉu forigas de la datumbazo ligitaj proponoj?
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('ĉefpaĝURLo')


def proponaldono(request, radikURLeraro):
    radiko = get_object_or_404(Radiko, eraro=radikURLeraro)
    if request.method == "POST":
        formularo = ProponoFormularo(request.POST)
        if formularo.is_valid():
            propono = formularo.save(commit=False)
            propono.por = radiko
            # TODO : Postaj aferoj
            propono.save()
            return redirect('radikpaĝURLo', radikURLeraro=radiko.eraro)
    else:
        formularo = ProponoFormularo()
    return render(request, 'vortaro/proponaldonpaĝo.html', {'formularo': formularo})


def proponforigo(request, radikURLeraro, proponURLeraro):
    radiko = get_object_or_404(Radiko, eraro=radikURLeraro)
    propono = get_object_or_404(Propono, por=radiko.pk, eraro=proponURLeraro)
    radiko_eraro = propono.por.eraro # Por konservi la eraro-n post la forigo
    propono.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('radikpaĝURLo', radikURLeraro=radiko_eraro)


# TODO : Kontroli ĉu la uzanto jam voĉdonis
def radikporo(request, radikURLeraro):
    radiko = get_object_or_404(Radiko, eraro=radikURLeraro)
    radiko.poroj = radiko.poroj + 1
    radiko.boneco = kalkuliBonecon(radiko.poroj, radiko.malporoj)
    radiko.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('radikpaĝURLo', radikURLeraro=radiko_eraro)


# TODO : Kontroli ĉu la uzanto jam voĉdonis
def radikmalporo(request, radikURLeraro):
    radiko = get_object_or_404(Radiko, eraro=radikURLeraro)
    radiko.malporoj = radiko.malporoj + 1
    radiko.boneco = kalkuliBonecon(radiko.poroj, radiko.malporoj)
    radiko.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('radikpaĝURLo', radikURLeraro=radiko_eraro)


# TODO : Kontroli ĉu la uzanto jam voĉdonis
def proponporo(request, radikURLeraro, proponURLeraro):
    radiko = get_object_or_404(Radiko, eraro=radikURLeraro)
    propono = get_object_or_404(Propono, por=radiko.pk, eraro=proponURLeraro)
    propono.poroj = propono.poroj + 1
    propono.boneco = kalkuliBonecon(propono.poroj, propono.malporoj)
    propono.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('radikpaĝURLo', radikURLeraro=radiko_eraro)


# TODO : Kontroli ĉu la uzanto jam voĉdonis
def proponmalporo(request, radikURLeraro, proponURLeraro):
    radiko = get_object_or_404(Radiko, eraro=radikURLeraro)
    propono = get_object_or_404(Propono, por=radiko.pk, eraro=proponURLeraro)
    propono.malporoj = propono.malporoj + 1
    propono.boneco = kalkuliBonecon(propono.poroj, propono.malporoj)
    propono.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('radikpaĝURLo', radikURLeraro=radiko_eraro)


def kalkuliBonecon(poroj, malporoj):
    return poroj / (poroj + malporoj)