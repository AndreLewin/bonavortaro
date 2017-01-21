from django.shortcuts import render

# Create your views here.
def ĉefpaĝo(request):
    return render(request, 'vortaro/ĉefpaĝo.html', {})