from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_project.settings')

app = Celery('site_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.beat_schedule = {
#     'msg-every-5-seconds': {
#         'task': 'mqtt_app.tasks.mqtt_test',
#         'schedule': 5,
#         'args': ('celery beat calling worker task', )
#     },
# }
# app.conf.timezone = 'UTC'
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()