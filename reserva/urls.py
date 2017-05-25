from django.conf.urls import url
from views import crearReserva_view, listarReserva_view, editarReserva_view

urlpatterns = [
    url(r'^crearreserva$', crearReserva_view, name='crear_reserva'),
    url(r'^listarreserva$', listarReserva_view, name='listar_reserva'),
    url(r'^editarreserva/(?P<id_reserva>\d+)/$', editarReserva_view, name='editar_reserva'),
]

