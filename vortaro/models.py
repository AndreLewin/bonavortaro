from django.db import models


class Radiko(models.Model):
    eraro = models.CharField(max_length=30, unique=True, default=None)
    poroj = models.FloatField(default=0)
    malporoj = models.FloatField(default=0)
    boneco = models.FloatField(default=0.5)

    oficialeco = models.CharField(max_length=2, default='X')
    duolingeco = models.BooleanField(default=False)
    oftecrango = models.IntegerField(default=0)

    plendoj = models.IntegerField(default=0)

    def __str__(self):
        return self.eraro


class Propono(models.Model):
    por = models.ForeignKey('vortaro.Radiko', related_name='proponoj')
    eraro = models.CharField(max_length=30, unique=True, default=None)
    poroj = models.FloatField(default=0)
    malporoj = models.FloatField(default=0)
    boneco = models.FloatField(default=0.5)

    plendoj = models.IntegerField(default=0)

    class Meta:
        unique_together = ('por','eraro')

    def __str__(self):
        return self.eraro