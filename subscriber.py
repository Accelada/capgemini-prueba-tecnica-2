import paho.mqtt.client as mqtt
import psycopg2
import os

# Conexión a PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("PG_HOST"),
    dbname=os.getenv("PG_DB"),
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD"),
)
conn.autocommit = True
cur = conn.cursor()


# Conexión al callback
def on_connect(client, userdata, flags, rc):
    """
    Se ejecuta cuando el cliente MQTT intenta conectar.
    - rc == 0: conexión exitosa.
    - rc != 0: error de conexión (código distinto de cero).
    """
    if rc == 0:
        print("Connected with result code " + str(rc))
        client.subscribe(os.getenv("TOPIC"))
    else:
        print(f"Connect failed with code {rc}")


def on_message(client, userdata, msg):
    """
    Se ejecuta cada vez que llega un mensaje al topic suscrito.
    msg.payload contiene los datos en bytes.
    """
    try:
        n = int(msg.payload.decode())
        sq = n * n

        try:
            cur.execute(
                "INSERT INTO results(val, val_squared) VALUES (%s, %s)",
                (n, sq),
            )

            print(f"Received {n}, stored square {sq}")

        except Exception as e:
            print(f"Error in insertion: {e}")

    except Exception as e:
        print("Error:", e)


# Configuración del cliente MQTT
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    os.getenv("MQTT_BROKER"),
    int(os.getenv("MQTT_PORT")),
    int(os.getenv("MQTT_KEEPALIVE")),
)

client.loop_forever()
