from django.test import TestCase
from recurso.models import Mantenimiento, recurso, Tipo_de_recurso, EstadoRecurso, tipoMantenimiento, estadoMantenimiento

# Create your tests here.


class MantenimientoTestCase(TestCase):
    def setUp(self):
        tiporecurso1 = Tipo_de_recurso.objects.create(nombre="Proyector", descripcion="Es un proyector")
        estadorecurso1 = EstadoRecurso.objects.create(estado="Disponible", descripcion="Esta disponible")
        recurso1 = recurso.objects.create(nombre="Proyector123456", estado=estadorecurso1, tipo=tiporecurso1)
        tipomantenimiento1 = tipoMantenimiento.objects.create(nombre="Preventivo")
        estadomantenimiento1 = estadoMantenimiento.objects.create(nombre="A realizar")
        mantenimiento1 = Mantenimiento.objects.create(estado=estadomantenimiento1, tipo=tipomantenimiento1,
                                                      descripcion="cambio de pantalla", fecha_inicio="2018-02-01 02:10:00+00:00",
                                                      fecha_fin="2019-02-02 03:10:00+00:00", cod_recurso=recurso1.id)


    def test_Mantenimiento_estado_nombre(self):
        estadomantenimiento1 = estadoMantenimiento.objects.create(nombre="A realizar")
        mantenimiento1 = Mantenimiento.objects.get(descripcion="cambio de pantalla")
        self.assertEqual(mantenimiento1.estado.nombre, estadomantenimiento1.nombre)
