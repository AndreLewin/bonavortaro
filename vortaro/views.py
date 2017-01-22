from django.shortcuts import render
from .models import Radiko

# Create your views here.
def ĉefpaĝo(request):
    radikoaro = Radiko.objects.order_by('malporoj') # Xoaro = array de Xo
    return render(request, 'vortaro/ĉefpaĝo.html', {'radikoaro': radikoaro})