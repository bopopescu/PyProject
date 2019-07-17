from __future__ import absolute_import, unicode_literals
import os
import django
from celery import Celery
from django.conf import settings
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VMwareAutoApi.settings') #���������ļ�
django.setup()

app = Celery('VMwareAutoApi')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')  #�ƶ�celery�����ļ�

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #����

app.conf.result_backend = 'redis://10.2.2.6:6379/0' #�������

