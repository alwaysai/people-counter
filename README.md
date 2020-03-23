# People counter + balenaSense demo

This project combines [balenaSense](https://github.com/balenalabs/balena-sense/) with the [people counter demo](https://github.com/alwaysai/people-counter/) from alwaysAI.
It creates a grafana dashboard that shows the video stream from alwaysAI with aditional metrics.

## Required hardware
- [Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
- A [DC barrel jack power supply](https://www.adafruit.com/product/1466) with 5.5mm OD / 2.1mm ID / 9.5mm length, center pin positive that can supply up to 5V⎓4A
- A [jumper](https://www.adafruit.com/product/3525) to short J48
- A [USB Webcam](https://www.amazon.com/Logitech-Desktop-Widescreen-Calling-Recording/dp/B004FHO5Y6/ref=sr_1_4?keywords=logitech+webcam+usb&qid=1582050432&sr=8-4) or an IP camera which supplies an RTSP feed
- A [WiFi USB dongle](https://www.amazon.com/TP-Link-wireless-network-Adapter-SoftAP/dp/B008IFXQFU/ref=sr_1_3?keywords=usb+wifi+adapter&qid=1582050405&sr=8-3)

## Before you start

1. Plug the USB webcam (unless you are using an IP camera) and the USB WiFi dongle into the Jetson Nano
2. Fit a jumper to J48 on the Jetson Nano board ([instructions](https://devtalk.nvidia.com/default/topic/1048640/jetson-nano/power-supply-considerations-for-jetson-nano-developer-kit/))
3. Flash the SD card, and you are good to go!


## Usage: Visualization

To visualize statistics and a video stream:

- Grafana: http://deviceLocalIP
- alwaysAI: http://deviceLocalIP:5000

Note that the grafana dashboard will show both stats and the alwaysAI stream so it's better for a live demo.


## Usage: Change object detection model

You can change the model that is used to perform object detection via the `OBJECT_DETECTION_MODEL` environment variable:

| Neural Network Framework | Dataset | Model | OBJECT_DETECTION_MODEL value | Reference inference time |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| caffe | COCO | MobileNet SSD | mobilenet_ssd (default) | 400 msec |
| darknet | COCO | Yolo v2 tiny | yolo_v2_tiny | 60 msec |
| darknet | VOC0712 | Yolo v2 tiny | yolo_v2_tiny_voc | 70 msec |
| darknet | COCO | Yolo v3 tiny | yolo_v3_tiny | 60 msec |

## Usage: Use an IP camera

You can add an RSTP feed url via the `IP_CAMERA_FEED` environment variable. Examples:

```rtsp://192.168.1.10:88```

With a video stream defined:

```rtsp://192.168.1.10:88/mainVideo```

Feed with authentication:

```rtsp://username:password@192.168.1.10```


