# expociencia/models/usuario.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('coordinador', 'Coordinador'),
        ('jurado', 'Jurado'),
        ('administrador', 'Administrador'),
        ('expositor', 'Expositor'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES)
    registro = models.CharField(max_length=20, unique=True)
