import os
import time
import random
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print(f"Connect failed with code {rc}")


def on_publish(client, userdata, mid):
    print(f"Message {mid} published")


client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(
    os.getenv("MQTT_BROKER"),
    int(os.getenv("MQTT_PORT")),
    int(os.getenv("MQTT_KEEPALIVE")),
)

try:
    topic = os.getenv("TOPIC")
    interval = int(os.getenv("INTERVAL"))

    while True:
        client.publish(topic, str(random.randint(0, 100)))
        time.sleep(interval)

except KeyboardInterrupt:
    client.disconnect()
