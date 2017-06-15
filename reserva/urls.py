from django.conf.urls import url
from views import calcular_view, crearReserva_view, listarReserva_view, editarReserva_view, listarListaReserva_view, crearReservaGeneral_view

urlpatterns = [
    url(r'^crearreserva$', crearReserva_view, name='crear_reserva'),
    url(r'^listarreserva$', listarReserva_view, name='listar_reserva'),
    url(r'^editarreserva/(?P<id_reserva>\d+)/$', editarReserva_view, name='editar_reserva'),
    url(r'^listarlistareserva$', listarListaReserva_view, name='listar_lista_reserva'),
    url(r'^calcularlistareserva/(?P<id_lista>\d+)/$', calcular_view, name='calcular_reserva'),
    url(r'^crearreservageneral$', crearReservaGeneral_view, name='crear_reservageneral'),
]

