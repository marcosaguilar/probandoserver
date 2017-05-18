from django.test import TestCase
from recurso.models import Mantenimiento

# Create your tests here.


class MantenimientoTestCase(TestCase):
    def setUp(self):
        mantenimiento1=Mantenimiento.objects.create(nombre="reparacion1",descripcion="cambio de pantalla",fechainicio="2018-02-01 2:10:00",fechafin="2019-02-02 3:10:00")

    def test_Mantenimiento_descripcion(self):
        mantenimiento1 = Mantenimiento.objects.get(nombre="reparacion1")
        self.assertEqual(mantenimiento1.descripcion, "cambio de pantalla")
