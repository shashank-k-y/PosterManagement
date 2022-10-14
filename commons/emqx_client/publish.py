# python 3.8

import random

from paho.mqtt import client as mqtt_client
from django.conf import settings


broker = settings.MQTT_BROKER
port = 1883
topic = "PosterManagement"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = settings.MQTT_USERNAME
password = settings.MQTT_PASSWORD


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, message):
    result = client.publish(topic, message)
    status = result[0]
    if status == 0:
        print(f"Send message: `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def run(message):
    client = connect_mqtt()
    publish(client, message)
