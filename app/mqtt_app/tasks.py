from __future__ import absolute_import, unicode_literals

from celery.schedules import crontab
from celery import shared_task

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()

# Estas tareas son las que el consumer delega para ser ejecutadas por los workers de celery.
# Aquí idealmente Celery debe pre-procesar los datos y seleccionar el controlador/view adecuado
# para que interactúe con el modelo. En última instancia la lógica de tratar con el modelo debe
# permanecer en cada app y simplemente ser llamada desde aquí.
@shared_task(bind=True)
def mqtt_test(self, msg):
    print(f"Celery task say: \"{msg}\"")

    # Así se puede publicar desde la aplicación, a través de la capa de canales
    # hacia el broker mqtt.
    async_to_sync(channel_layer.send)('mqtt', {
        'type': 'mqtt.pub',
        'text': {
            'topic': 'testmq',
            'payload': f"{msg} - {self.request.id}"
        }
    })