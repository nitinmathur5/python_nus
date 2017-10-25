#Team A = SAVIOUR
#publisher
# should listen to listen on this topic help
# if there are any messages, you should send to slack

import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("10.20.10.106", 7000, 60) #broker was created by bala - is the mqtt host name
#client.publish("911", "help")
client.publish("911", "help")
#forward this message to slack client now

from slackclient import SlackClient
def sendMessageToSlack(msg):
    slack_token = "xoxb-259967078277-O0ZnHWiXcTi8t4tctwcVV8cY"
    sc = SlackClient(slack_token)
    resp= sc.api_call("chat.postMessage", channel="#saviour", text=msg)

sendMessageToSlack("Nitin: help")
'''
class myClient():
    def __init__(self, x):
        self.x = x
    def onconnect(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def onmessage(self, message, payload):
        self.message = message
        self.payload = payload

    def loop_forever(self):
        self.onconnect("bala", "password")
        time.sleep(5)
        self.onmessage("Yo", "Wellcomme")

c = myClient("10")

def myConnect(user,pwd):
    print ("MY impl of My connect")

c.onconnect = myConnect("nitin", "nitin")

#c.onconnect("nitin", "nitin")
'''