#/usr/bin/python
# -*- coding: utf-8 -*-

#"""
#WSGI config for electrolab project.
#
#It exposes the WSGI callable as a module-level variable named ``application``.
#
#For more information on this file, see
#https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
#"""
#
#import os
#
#from django.core.wsgi import get_wsgi_application
#
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "electrolab.settings")
#
#application = get_wsgi_application()


import os, sys

# В python path добавляется директория проекта
dn = os.path.dirname
PROJECT_ROOT = os.path.abspath(dn(dn(__file__)))
DJANGO_PROJECT_ROOT = os.path.join(PROJECT_ROOT, 'apps')
sys.path.append(DJANGO_PROJECT_ROOT)

# Установка файла настроек
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Запуск wsgi-обработчика
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
