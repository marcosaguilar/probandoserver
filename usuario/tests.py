from django.test import TestCase
from usuario.models import usuario, rol, prioridad
from recurso.models import Tipo_de_recurso
from django.contrib.auth.models import Permission


# Create your tests here.

class UsuarioTestCase(TestCase):
    def setUp(self):
        permisos = Permission.objects.all()
        tipo=Tipo_de_recurso.objects.create(nombre="Laboratorio",descripcion="Sala de laboratorio")
        rol1 = rol.objects.create(nombre = "administrador de recursos de laboratorio",tipoRecurso=tipo)
        rol1.permisos.add(permisos[0])
        usuario1 = usuario.objects.create(username = "alumno",password="admin", cedula=123,
                                          nombres="marcos",apellidos="aguilar",email="marcosaguilarn91@gmail.com",
                                          telefono=456, direccion="herminio", prioridad=1)
        usuario1.rol.add(rol1)

    def test_usuario_telefono(self):
        usuario1 = usuario.objects.get(nombres="marcos")
        self.assertEqual(usuario1.telefono, '456')

    def test_usuario_cedula(self):
        usuario1 = usuario.objects.get(nombres="marcos")
        self.assertEqual(usuario1.cedula, 123)

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
