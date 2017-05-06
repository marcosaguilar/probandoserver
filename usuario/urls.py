from django.conf.urls import url
from views import index, crearUsuario_view, crearRol_view, listarUsuario_view ,editarUsuario_view
from views import eliminarUsuario_view, listarRol_view, editarRol_view, eliminarRol_view

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^crearusuario$', crearUsuario_view, name='crearUsuario_crear'),
    url(r'^crearrol$', crearRol_view, name='crearRol_crear'),
    url(r'^listarusuario$',listarUsuario_view ,name='listar_usuario'),
    url(r'^editarusuario/(?P<id_usuario>\d+)/$', editarUsuario_view, name='editar_usuario'),
    url(r'^eliminarusuario/(?P<id_usuario>\d+)/$', eliminarUsuario_view, name='eliminar_usuario'),
    url(r'^listarrol$', listarRol_view, name='listar_rol'),
    url(r'^editarrol/(?P<id_rol>\d+)/$', editarRol_view, name='editar_rol'),
    url(r'^eliminarrol/(?P<id_rol>\d+)/$', eliminarRol_view, name='eliminar_rol'),
]