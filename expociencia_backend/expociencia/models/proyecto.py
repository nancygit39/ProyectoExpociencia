from django.db import models
from .feria import Feria

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    archivo_pdf = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=50)
    feria = models.ForeignKey(Feria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
