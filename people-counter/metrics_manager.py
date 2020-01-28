import time
import paho.mqtt.client as mqtt
import json

'''
ALL_USERS schema
{ object_id : time }
'''

class MetricsManager:

    def __init__(self):
        self.ACTIVE_IDs = []
        self.START = int(time.time())
        self.ALL_USERS = {}
        
        # MQTT sends data to balenaSense
        self.mqtt = mqtt.Client()
        self.mqtt.connect("mqtt", 1883, 60)
        self.mqtt.on_connect = self.on_connect
        self.mqtt.on_message = self.on_message

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    def newLoop(self):
        self.ACTIVE_IDs = []
        self.START = int(time.time())

    def currentTimeFromStart(self):
        now = int(time.time())
        elapsed = now - self.START
        return elapsed

    def addTimeFor(self, objectId):
        elapsed = self.currentTimeFromStart()
        if not objectId in self.ALL_USERS:
            self.ALL_USERS[objectId] = elapsed
            
            # If new person detected, send to balenaSense
            data=json.dumps({"sepalLength": "6.4","sepalWidth":  "3.2","petalLength": "4.5","petalWidth":  "1.5"})
            self.mqtt.publish('sensors', payload=data, qos=0, retain=False)
        else:
            self.ALL_USERS[objectId] += elapsed
        # sendTrackDataToServer(objectId, elapsed)

    def timeForId(self, objectId):
        return self.ALL_USERS[objectId]

    def currentMetrics(self):
        times = []
        for _, time in self.ALL_USERS.items():
            times.append(time)
        if len(times) == 0:
            times.append(0)
        return {
            "min": min(times),
            "max": max(times),
            "avg": sum(times) / len(times),
            "total": sum(times),
            "count": len(self.ALL_USERS.items())
        }
