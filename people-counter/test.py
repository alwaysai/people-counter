import paho.mqtt.publish as publish
import json

# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
#     data=json.dumps({"sepalLength": "6.4","sepalWidth":  "3.2","petalLength": "4.5","petalWidth":  "1.5"})
#     mqtt.publish('sensors', payload=data, qos=0, retain=False)

# def on_message(client, userdata, msg):
#     print(msg.topic+" "+str(msg.payload))

# mqtt = mqtt.Client()
# mqtt.connect("mqtt", 1883, 60)
# mqtt.on_connect = on_connect
# mqtt.on_message = on_message

# publish.single("paho/test/single", payload=json.dumps(mode_msg), qos=2, hostname="localhost", port=4444)

publish.single("sensors", payload=json.dumps({"humidity" : 80}), qos=2, hostname="mqtt", port=1883)
