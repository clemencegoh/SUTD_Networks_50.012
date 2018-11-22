#!/usr/bin/env python
# 50.012 Lab 9 skeleton script
# Nils, SUTD, 2016
# based on https://sakshambhatla.wordpress.com/2014/08/11/simple-mqtt-broker-and-client-in-python/
# Modified by: Clemence Goh (1002075)
import paho.mqtt.client as mqtt

import cmd
import sys
import time
import select
import threading
from queue import Queue

username = "clemence"
broker = "test.mosquitto.org"
port = 1883
# default channel subscriptions
dchannels = ['hello/world', 'user/'+username, 'hello/'+username]
# dchannels = ['user/'+username]
interrupt_thread = Queue()
message_QoS = 0
retained_flag = False

help_msg = "Welcome to the MQTT client CLI.\n" \
          "Please type in any message to broadcast to all current topics.\n" \
          "Custom options are:\n" \
          "1. Help\n" \
          "2. Send to someone\n" \
          "3. Subscribe/Unsubscribe to topic\n" \
          "4. Check current subscribed topics\n" \
          "5. Set QoS = 0\n" \
          "6. Set QoS = 1\n" \
          "7. Set QoS = 2\n" \
          "8. Set/Unset retained flag\n" \
          "9. Exit"


def subscribe(client, topic):
    client.subscribe(topic)


# The callback for when the client receives a CONNACK response from the server.
# auto-subscribes to default channels
def on_connect(client, userdata, flags, rc):
        if rc == mqtt.MQTT_ERR_SUCCESS:
                print("Connected successfully to %s" % broker)
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        for dc in dchannels:
                print("Subscribing to channel %s" % dc)
                subscribe(client, dc)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    m = "Message received on topic: {}, using QoS {}\nMessage: {}".format(msg.topic,str(msg.qos),str(msg.payload))
    # receive.put(m)
    print(m)


def checkCommand(_in):
    try:
        val = int(_in)
        return True, val
    except ValueError:
        return False, 0


class cli:
    """Simple MQTT chat self.client."""

    def __init__(self, _client):
        self.client = _client
        self.looping = True

    def broadcast(self, msg):
        for channel in dchannels:
            self.client.publish(channel, msg)

    def do_msg(self, person):
        "send hello message to user/<person>"
        if person:
            greeting = "hello %s" % (person)
        else:
            greeting = 'hello'
        print("Sending %s to %s"%(greeting,"user/"+person))
        self.broadcast(greeting)

    def personal_msg(self, person, msg):
        if msg and person:
            self.client.publish("user/"+person, msg, message_QoS)
    
    def do_quit(self, line):
            print("Goodbye!")
            exit(0)

    def processInput(self, _input):
        global message_QoS, dchannels, retained_flag
        # input is a string
        isCustom, val = checkCommand(_input)
        if isCustom:
            if val == 1:
                # Help message
                print(help_msg)
                return
            if val == 2:
                # Send to someone
                specific_user = input("Person =>")
                message = input("Message =>")
                print("sending {} to {}...".format(message, "user/"+specific_user))
                self.personal_msg(specific_user, message)
                return
            if val == 3:
                # subscribe/unsub
                topic = input("Please input topic =>")
                if topic in dchannels:
                    dchannels.remove(topic)
                    self.client.unsubscribe(topic)
                    print(topic, "unsubscribed")
                else:
                    dchannels.append(topic)
                    self.client.subscribe(topic)
                    print(topic, "subscribed")
                return
            if val == 4:
                print(dchannels)
                return
            if val == 5:
                message_QoS = 1
                return
            if val == 6:
                message_QoS = 2
                return
            if val == 7:
                message_QoS = 3
                return
            if val == 8:
                retained_flag = not retained_flag
                return
            if val == 9:
                self.do_quit("")
            else:
                print("Please enter a valid number")
                return
        else:
            # broadcast
            self.broadcast(_input)


def processQueue(client):
    while True:
        client.loop_forever()


def start_connection(clean_session):
    global interrupt_thread
    print("connecting...")
    client = mqtt.Client(username, clean_session)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port, 60)
    time.sleep(1)

    c = cli(client)

    print(help_msg)
    # If there's input ready, do something, else do something
    # else. Note timeout is zero so select won't block at all.

    # set thread to listen to updates
    t = threading.Thread(target=processQueue, args=(client,))
    t.daemon = True
    t.start()

    while True:
        i = input("=>")

        # parses input for other custom options
        c.processInput(i)

    # while sys.stdin in select.select([sys.stdin], [], [], 0):
    #     line = sys.stdin.readline()
    #     if line:
    #         cli().onecmd(line)
    #     else:  # an empty line means stdin has been closed
    #         print('eof')
    #         exit(0)
    # else:
    #     self.client.loop(1)


if __name__ == '__main__':
    start_connection(False)
