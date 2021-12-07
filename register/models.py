from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    latitud = models.CharField(max_length=60)
    longitud = models.CharField(max_length=60)
    birthDate = models.DateField()
    email = models.EmailField(max_length = 200, unique=True)
    institution = models.CharField(max_length=100)
    dirección = models.CharField(max_length=250)
    status = models.BooleanField(default=False)


class InstitutionModel(models.Model):
    name = models.CharField(max_length=250)
