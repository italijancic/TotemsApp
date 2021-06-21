import datetime
from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer

# Aquí se reciben y se envían los datos recibidos a través de la capa de canales que
# está adaptada como interfaz MQTT. Para eso se cuenta con los dos métodos, dentro de los cuales
# se define qué acción tomar cuando se reciben datos de algún tópico al que nos hallamos suscripto mediante
# chasgimqtt, o qué acción tomar previo a publicar información en un determinado tópico.
# Idealmente aquí lo único que debería ocurrir es un proceso de diferenciación de tópicos y luego delegar a celery.
class MqttConsumer(SyncConsumer):

    def mqtt_sub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        # do something with topic and payload
        print("subscribed topic: {0}, payload: {1}".format(topic, payload))

    def mqtt_pub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        # do something with topic and payload
        print("published topic: {0}, payload: {1}".format(topic, payload))