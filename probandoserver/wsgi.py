"""
WSGI config for probandoserver project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

#path a donde esta el manage.py de nuestro proyecto Django
sys.path.append("/home/ubuntu/Desktop/probandoserver/")

os.environ["DJANGO_SETTINGS_MODULE"] = "probandoserver.settings"

#prevenimos UnicodeEncodeError
os.environ.setdefault("LANG", "en_US.UTF-8")
os.environ.setdefault("LC_ALL", "en_US.UTF-8")

application = get_wsgi_application()
