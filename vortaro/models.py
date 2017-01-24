from django.db import models


class Radiko(models.Model):
    eraro = models.CharField(max_length=30, unique=True)
    poroj = models.FloatField(default=0)
    malporoj = models.FloatField(default=0)

    oficialeco = models.CharField(max_length=2, default='X')
    duolingeco = models.BooleanField(default=False)
    oftecrango = models.IntegerField(default=0)

    def __str__(self):
        return self.radikaro

class Propono(models.Model):
    por = models.ForeignKey('vortaro.Radiko', related_name='proponoj')
    per = models.ForeignKey('vortaro.Radiko', related_name='proponojDe')

    poroj = models.FloatField()
    malporoj = models.FloatField()