from django.db import models

# Create your models here.

class Registros(models.Model):
     dia = models.IntegerField()
     mes = models.IntegerField()
     ano = models.IntegerField()
     hora = models.IntegerField()
     minuto = models.IntegerField()
     segundo = models.IntegerField()
