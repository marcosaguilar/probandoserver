from django.test import TestCase
from usuario.models import usuario, rol
from recurso.models import Tipo_de_recurso
from django.contrib.auth.models import Permission


# Create your tests here.


class RolTestCase(TestCase):
    def setUp(self):
        permisos = Permission.objects.all()
        tipo=Tipo_de_recurso.objects.create(nombre="Laboratorio",descripcion="Sala de laboratorio")
        rol1 = rol.objects.create(nombre = "administrador de recursos de laboratorio",tipoRecurso=tipo)
        rol1.permisos.add(permisos[0])

    def test_rol_descripcion(self):
        rol1 = rol.objects.get(nombre="administrador de recursos de laboratorio")
        tipo = Tipo_de_recurso.objects.get(nombre="Laboratorio")
        self.assertEqual(rol1.tipoRecurso.descripcion, tipo.descripcion)
