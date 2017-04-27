from django.conf.urls import url

from views import index, crearUsuario_view, crearRol_view

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^crearusuario$', crearUsuario_view, name='crearUsuario_crear'),
    url(r'^crearrol$', crearRol_view, name='crearRol_crear'),
]