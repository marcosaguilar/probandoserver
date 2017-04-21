from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class usuario(AbstractUser):
    username = models.CharField(primary_key=True,max_length=20)
    password = models.CharField(max_length=10)
    cedula = models.IntegerField()
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=30)
