import time
import paho.mqtt.publish as publish
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
            print("New person detected!")
            publish.single("sensors", payload=json.dumps({"person" : 1}), qos=2, hostname="mqtt", port=1883)

        else:
            self.ALL_USERS[objectId] += elapsed

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
