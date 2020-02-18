import paho.mqtt.publish as publish
import json

publish.single("sensors", payload=json.dumps({"humidity" : 80}), qos=2, hostname="mqtt", port=1883)
