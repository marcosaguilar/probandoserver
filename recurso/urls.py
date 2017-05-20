from django.conf.urls import url


from views import index, crearMantenimiento_view, listarRecursoMantenimiento_view,listarAsignarMantenimiento_view
from views import crearTipo_Recurso_view, listarTipoRecurso_view, eliminarTipoRecurso_view
from views import crearRecurso_view,listarRecurso_view,eliminarRecurso_view,editarRecurso_view,editarMantenimiento_view
from views import listarMantenimiento_view

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^crearrecurso$', crearRecurso_view, name='crear_recurso'),
    url(r'^listarrecurso$', listarRecurso_view, name='listar_recurso'),
    url(r'^eliminarrecurso/(?P<id_recurso>\d+)/$', eliminarRecurso_view, name='eliminar_recurso'),
    url(r'^editarrecurso/(?P<id_recurso>\d+)/$', editarRecurso_view, name='editar_recurso'),

    url(r'^crearmantenimiento/(?P<id_recurso>\d+)/$', crearMantenimiento_view, name='crear_mantenimiento'),
    url(r'^listarrecursoymantenimiento$', listarRecursoMantenimiento_view, name='listar_rec_man'),
    url(r'^listarasignarman$', listarAsignarMantenimiento_view, name='listar_asignar_man'),

    url(r'^creartiporecurso$', crearTipo_Recurso_view, name='crear_tipo_recurso'),
    url(r'^listartiporecurso$', listarTipoRecurso_view, name='listar_tiporecurso'),
    url(r'^eliminartiporecurso/(?P<id_Tipo_de_recurso>\d+)/$', eliminarTipoRecurso_view, name='eliminar_tiporecurso'),
    url(r'^editarmantenimiento/(?P<id_mantenimiento>\d+)/$', editarMantenimiento_view, name='editar_mantenimiento'),
    url(r'^listarmantenimiento$', listarMantenimiento_view, name='listar_mantenimiento'),
]