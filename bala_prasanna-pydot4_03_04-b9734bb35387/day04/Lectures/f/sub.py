#Team B = 911
# subscriber - 
# if you receive a message continaing [danger, help, seeking help, I need help], it
#should publish a message to topic HELP

#Team A -- saviour
#publisher
# should listen to listen on this topic help
# if there are any messages, you should send to slack

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print ("Connected with result code " + str(rc))
    client.subscribe("911")

def on_message(client, userdata, msg):
    decoded_msg = msg.payload.decode()
    print(decoded_msg)
    if (decoded_msg == "danger" or decoded_msg == "help" or decoded_msg == "I need help"):
        client.connect("10.20.10.106",7000,60) #connect to broker
        client.publish("saviour", "help Nitin");
        
        from slackclient import SlackClient
        def sendMessageToSlack(msg):
            slack_token = "xoxb-259967078277-O0ZnHWiXcTi8t4tctwcVV8cY"
            sc = SlackClient(slack_token)
            resp= sc.api_call("chat.postMessage", channel="#saviour", text=msg)

        sendMessageToSlack("Nitin: help" + decoded_msg)
        


client = mqtt.Client()
client.connect("10.20.10.106",7000,60) #connect to broker
client.on_connect = on_connect  #--> callback function
client.on_message = on_message
client.loop_forever()

#client.disconnect();