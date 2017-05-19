from django.conf.urls import url
from views import crearRecurso_view, index, listarRecurso_view, eliminarRecurso_view, editarRecurso_view
from views import crearMantenimiento_view, listarMantenimiento_view,listarAsignarMantenimiento_view

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^crearrecurso$', crearRecurso_view, name='crear_recurso'),
    url(r'^listarrecurso$', listarRecurso_view, name='listar_recurso'),
    url(r'^eliminarrecurso/(?P<id_recurso>\d+)/$', eliminarRecurso_view, name='eliminar_recurso'),
    url(r'^editarrecurso/(?P<id_recurso>\d+)/$', editarRecurso_view, name='editar_recurso'),
    url(r'^crearmantenimiento/(?P<id_recurso>\d+)/$', crearMantenimiento_view, name='crear_mantenimiento'),
    url(r'^listarrecursoymantenimiento$', listarMantenimiento_view, name='listar_rec_man'),
    url(r'^listarasignarman$', listarAsignarMantenimiento_view, name='listar_asignar_man'),
]