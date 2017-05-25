from __future__ import unicode_literals
from django.contrib.auth.models import Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser
from recurso.models import Tipo_de_recurso


# Create your models here.


class rol(models.Model):
    """este modelo contiene los atributos de un rol"""
    nombre = models.CharField(max_length=50)
    #descripcion = models.CharField(max_length=100)
    permisos = models.ManyToManyField(Permission)
    tipoRecurso = models.ForeignKey(Tipo_de_recurso, null=True, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return '{}'.format(self.nombre)

    def get_tipoRecurso(self):
        return self.tipoRecurso

    class Meta:
        permissions = (
            ("ver_rol", "Puede ver los roles disponibles"),
        )


class usuario(AbstractUser):
    """este modelo contiene los atributos de un usuario"""
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=500)
    cedula = models.IntegerField(null=True, blank=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=50)
    rol = models.ManyToManyField(rol)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','cedula']

    def get_rol(self):
        return self.rol


    class Meta:
        permissions = (
            ("ver_usuario", "Puede ver los usuarios disponibles"),
        )