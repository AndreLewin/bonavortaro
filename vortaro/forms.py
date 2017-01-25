from django import forms

from .models import Radiko

class RadikoFormularo(forms.ModelForm):

    class Meta:
        model = Radiko
        fields = ('eraro',)