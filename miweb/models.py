from django.db import models

class sintomas(models.Model):
    edad = models.CharField(max_length=2)
    fiebre = models.CharField(max_length=2)
    tos = models.CharField(max_length=2)
    cansancio = models.CharField(max_length=2)
    aire = models.CharField(max_length=2)
    pecho = models.CharField(max_length=2)
    cabeza = models.CharField(max_length=2)
    respirar = models.CharField(max_length=2)

class enfermedad(models.Model):
    cancer = models.CharField(max_length=2)
    diabetes = models.CharField(max_length=2)
    hipertension = models.CharField(max_length=2)