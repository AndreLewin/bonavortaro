from django import forms
from .models import Radiko, Propono


class RadikoFormularo(forms.ModelForm):

    class Meta:
        model = Radiko
        fields = ('eraro',)


class ProponoFormularo(forms.ModelForm):

    class Meta:
        model = Propono
        fields = ('eraro',)