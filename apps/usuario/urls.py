from django.conf.urls import url, include

from views import index, usuario_view, crearRol_view

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^crearusuario$', usuario_view, name='usuario_crear'),
    url(r'^crearrol$', crearRol_view, name='crearRol_crear'),
    # url('^', include('django.contrib.auth.urls')),
]