"""probandoserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from probandoserver.views import login_page, homepage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^login',login_page, name="login_page"),
    url(r'^$',homepage, name="home_page"),
    url(r'^usuario/', include('apps.usuario.urls',namespace="usuario")),
    url(r'^recurso/', include('apps.recurso.urls')),
=======
    url(r'^$',login_page, name="login_page"),
    url(r'^usuario/', include('usuario.urls')),
    url(r'^recurso/', include('recurso.urls')),
>>>>>>> developerMA
]
