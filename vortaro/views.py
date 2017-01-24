from django.shortcuts import render, get_object_or_404
from .models import Radiko

# Create your views here.
def ĉefpaĝo(request):
    radikoaro = Radiko.objects.order_by('malporoj') # Xoaro = array de Xo
    return render(request, 'vortaro/ĉefpaĝo.html', {'radikoaro': radikoaro})

def radikpaĝo(request, URLeraro):
    radiko = get_object_or_404(Radiko, eraro=URLeraro)
    return render(request, 'vortaro/radikpaĝo.html', {'radiko': radiko})