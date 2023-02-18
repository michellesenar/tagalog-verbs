"""
WSGI config for frverbs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

application = get_wsgi_application()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frverbs.settings")

application = WhiteNoise(application, root="/static/")
application.add_files("/src/verbs/static/", prefix="more-files/")
