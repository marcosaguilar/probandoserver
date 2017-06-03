from django.test import TestCase
from recurso.models import recurso, Tipo_de_recurso, EstadoRecurso
from usuario.models import usuario
from reserva.models import reserva, estadoReserva ,listaReserva
from django.contrib.auth.models import User
import datetime
# Create your tests here.
class ReservaTestCase(TestCase):

    def setUp(self):

        tiporecurso1 = Tipo_de_recurso.objects.create(nombre="Proyector", descripcion="Es un proyector")
        estadorecurso1 = EstadoRecurso.objects.create(estado="Disponible", descripcion="Esta disponible")
        recurso1 = recurso.objects.create(nombre="Proyector123456", estado=estadorecurso1, tipo=tiporecurso1)
        usuario1 = usuario.objects.create_user(username="admin",password="admin",cedula=123,nombres="admin",
                                              apellidos="admin",email="admin@gmail.com",telefono=123,
                                              direccion="admin")

        listareserva1 = listaReserva.objects.create(fecha="2017-02-02", recurso=recurso1)
        estadoreserva1 = estadoReserva.objects.create(estado="A confirmar")
        reserva1 = reserva.objects.create(recurso=recurso1, tipo_recurso=tiporecurso1,
                                          usuario=usuario1, fecha_inicio="2017-02-07 1:10:00",
                                          fecha_fin="2017-02-07 02:10:00",
                                          estado_reserva=estadoreserva1,
                                          lista_reserva=listareserva1,
                                          gano_reserva=0,
                                          fechayhora="2017-02-02 03:10:00")

    def test_Reserva_estado_nombre(self):
        estadoreserva1 = estadoReserva.objects.create(estado="A confirmar")
        reserva1 = reserva.objects.get(gano_reserva=0)
        self.assertEqual(reserva1.estado_reserva.estado, estadoreserva1.estado)



    def test_Reserva_fecha_fin(self):
            reserva1 = reserva.objects.get(fecha_fin="2017-02-07 02:10:00")
            self.assertEqual(reserva1.fecha_fin.__str__(), "2017-02-07 02:10:00")


