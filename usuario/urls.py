from django.conf.urls import url
from views import index, crearUsuario_view, crearRol_view, listarUsuario_view ,editarUsuario_view, modificarRol_view
from views import eliminarUsuario_view

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^crearusuario$', crearUsuario_view, name='crearUsuario_crear'),
    url(r'^crearrol$', crearRol_view, name='crearRol_crear'),
    url(r'^listarusuario$',listarUsuario_view ,name='listar_usuario'),
    url(r'^editarusuario/(?P<id_usuario>\d+)/$', editarUsuario_view, name='editar_usuario'),
    url(r'^eliminarusuario/(?P<id_usuario>\d+)/$', eliminarUsuario_view, name='eliminar_usuario'),
    url(r'^modificarrol$', modificarRol_view, name='modificar_rol'),
]