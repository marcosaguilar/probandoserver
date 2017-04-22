from django.conf.urls import url

from views import crearRecurso_view, index


urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^crearrecurso$', crearRecurso_view, name='usuario_crear'),
]