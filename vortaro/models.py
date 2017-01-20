from django.db import models


class Radiko(models.Model):
    radikaro = models.CharField(max_length=200) # TODO : Devas esti aro de radikoj
    poroj = models.FloatField()
    malporoj = models.FloatField()

    oficialeco = models.CharField(max_length=2)
    duolingeco = models.BooleanField(default=False)
    rango = models.IntegerField(default=0)

    def __str__(self):
        return self.radikaro

class Propono(models.Model):
    por = models.ForeignKey('vortaro.Radiko', related_name='proponoj')
    per = models.ForeignKey('vortaro.Radiko', related_name='proponojDe')

    poroj = models.FloatField()
    malporoj = models.FloatField()