from django.test import TestCase
from usuario.models import usuario, rol
from django.contrib.auth.models import Permission


# Create your tests here.


class RolTestCase(TestCase):
    def setUp(self):
        permisos = Permission.objects
        rol.objects.create(nombre = "administrador de recursos", permisos = a1, tipoRecursos = "Resumen del libro")

    def test_libros_autor(self):
        libro1 = Libro.objects.get(titulo="Harry Potter")
        self.assertEqual(libro1.autor.nombre, "J.K. Rowling")  

    def test_libros_puntuacion(self):
        libro2 = Libro.objects.get(titulo="El Quijote")
        self.assertEqual(libro2.get_puntuacion_media(), 0)
