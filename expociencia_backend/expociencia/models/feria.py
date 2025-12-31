from django.db import models

class Feria(models.Model):
    gestion = models.CharField(max_length=10)
    año = models.IntegerField()
    version = models.CharField(max_length=200)
    cronograma = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    nombre = models.CharField(max_length=255)
    area = models.CharField(max_length=20)
    modalidades = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} ({self.año})"
