#/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

# В python path добавляется директория проекта
dn = os.path.dirname
PROJECT_ROOT = os.path.abspath( dn(dn(__file__)) )
DJANGO_PROJECT_ROOT = os.path.join(PROJECT_ROOT, 'electrolab')
sys.path.append( DJANGO_PROJECT_ROOT )

# Установка файла настроек
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Запуск wsgi-обработчика
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()