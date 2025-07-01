import os
import time
import random
import paho.mqtt.client as mqtt


# Conexión al callback
def on_connect(client, userdata, flags, rc):
    """
    Se ejecuta cuando el cliente MQTT intenta conectar.
    - rc == 0: conexión exitosa.
    - rc != 0: error de conexión (código distinto de cero).
    """
    if rc == 0:
        print("Connected successfully")
    else:
        print(f"Connect failed with code {rc}")


def on_publish(client, userdata, mid):
    """
    Se llama cuando un mensaje se ha enviado con éxito.
    - mid: identificador del mensaje publicado.
    """
    print(f"Message {mid} published")


# Configuración del cliente MQTT
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(
    os.getenv("MQTT_BROKER"),
    int(os.getenv("MQTT_PORT")),
    int(os.getenv("MQTT_KEEPALIVE")),
)

client.loop_start()

try:
    topic = os.getenv("TOPIC")
    interval = int(os.getenv("INTERVAL"))

    while True:
        client.publish(topic, str(random.randint(0, 100)))
        time.sleep(interval)

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
