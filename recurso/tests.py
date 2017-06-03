from django.test import TestCase
from recurso.models import Mantenimiento, recurso, Tipo_de_recurso, EstadoRecurso, tipoMantenimiento, estadoMantenimiento
import datetime
# Create your tests here.


class MantenimientoTestCase(TestCase):
    def setUp(self):
        tiporecurso1 = Tipo_de_recurso.objects.create(nombre="Proyector", descripcion="Es un proyector")
        estadorecurso1 = EstadoRecurso.objects.create(estado="Disponible", descripcion="Esta disponible")
        recurso1 = recurso.objects.create(nombre="Proyector123456", estado=estadorecurso1, tipo=tiporecurso1)
        tipomantenimiento1 = tipoMantenimiento.objects.create(nombre="Preventivo")
        estadomantenimiento1 = estadoMantenimiento.objects.create(nombre="A realizar")
        mantenimiento1 = Mantenimiento.objects.create(estado=estadomantenimiento1, tipo=tipomantenimiento1,
                                                      descripcion="cambio de pantalla", fecha_inicio="2018-02-01 02:10:00",
                                                      fecha_fin="2017-02-02 23:10:00", cod_recurso=recurso1.id)
        recurso2 = recurso.objects.create(nombre="Proyector789", estado=estadorecurso1, tipo=tiporecurso1, mantenimiento=mantenimiento1)


    def test_Mantenimiento_estado_nombre(self):
        estadomantenimiento1 = estadoMantenimiento.objects.create(nombre="A realizar")
        mantenimiento1 = Mantenimiento.objects.get(descripcion="cambio de pantalla")
        self.assertEqual(mantenimiento1.estado.nombre, estadomantenimiento1.nombre)


    def test_Mantenimiento_fecha_fin(self):
        mantenimiento1 = Mantenimiento.objects.get(descripcion="cambio de pantalla")
        self.assertEqual(mantenimiento1.fecha_fin.__str__(), "2017-02-02 23:10:00")


    def test_recurso_Mantenimiento(self):
        mantenimiento1 = Mantenimiento.objects.get(descripcion="cambio de pantalla")
        recurso2 = recurso.objects.get(nombre="Proyector789")
        self.assertEqual(mantenimiento1.descripcion, recurso2.mantenimiento.descripcion)


    def test_Mantenimiento_fecha_finb(self):
        mantenimiento1 = Mantenimiento.objects.get(descripcion="cambio de pantalla")
        #self.assertEqual(mantenimiento1.fecha_fin.time().__str__(), datetime.datetime.now().time().__str__())
        tiempo1 = datetime.datetime.combine(datetime.datetime.now().date(), datetime.datetime.now().time())
        tiempo2 = datetime.datetime.combine(mantenimiento1.fecha_fin.date(), mantenimiento1.fecha_fin.time())
        self.assertGreaterEqual(tiempo1.__str__(),tiempo2.__str__())

