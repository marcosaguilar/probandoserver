from django.conf.urls import url

from views import index, usuario_view

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^nuevo$', usuario_view,name='usuario_crear'),
]