from django.db import models
from django.forms import CharField

class Familiar(models.Model):
    name=models.CharField(max_length=255)
    surname=models.CharField(max_length=255)
    edad=models.IntegerField()
    nacimiento=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.surname}'