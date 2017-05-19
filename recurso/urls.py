from django.conf.urls import url
from views import crearRecurso_view, index, listarRecurso_view, eliminarRecurso_view, editarRecurso_view, crearTipo_Recurso_view, listarTipoRecurso_view, eliminarTipoRecurso_view


urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^crearrecurso$', crearRecurso_view, name='crear_recurso'),
    url(r'^listarrecurso$', listarRecurso_view, name='listar_recurso'),
    url(r'^eliminarrecurso/(?P<id_recurso>\d+)/$', eliminarRecurso_view, name='eliminar_recurso'),
    url(r'^editarrecurso/(?P<id_recurso>\d+)/$', editarRecurso_view, name='editar_recurso'),
    url(r'^creartiporecurso$', crearTipo_Recurso_view, name='crear_tipo_recurso'),
    url(r'^listartiporecurso$', listarTipoRecurso_view, name='listar_tiporecurso'),
    url(r'^eliminartiporecurso/(?P<id_Tipo_de_recurso>\d+)/$', eliminarTipoRecurso_view, name='eliminar_tiporecurso'),

]