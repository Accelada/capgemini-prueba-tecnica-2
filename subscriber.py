import paho.mqtt.client as mqtt
import psycopg2
import os

# from dotenv import load_dotenv

# load_dotenv()

# Conexión a PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("PG_HOST"),
    dbname=os.getenv("PG_DB"),
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD"),
)
conn.autocommit = True
cur = conn.cursor()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(os.getenv("TOPIC"))


def on_message(client, userdata, msg):
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


client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    os.getenv("MQTT_BROKER"),
    int(os.getenv("MQTT_PORT")),
    int(os.getenv("MQTT_KEEPALIVE")),
)
client.loop_forever()
