"""
WSGI config for storehiro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

#Este archivo nos permitira hacer deploy del proyecto

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storehiro.settings')

application = get_wsgi_application()
