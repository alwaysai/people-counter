# Say hi to your chickens

## Required hardware
- [Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
- A [DC barrel jack power supply](https://www.adafruit.com/product/1466) with 5.5mm OD / 2.1mm ID / 9.5mm length, center pin positive that can supply up to 5V⎓4A
- A [jumper](https://www.adafruit.com/product/3525) to short J48
- A [USB Webcam](https://www.amazon.com/Logitech-Desktop-Widescreen-Calling-Recording/dp/B004FHO5Y6/ref=sr_1_4?keywords=logitech+webcam+usb&qid=1582050432&sr=8-4)
- A [WiFi USB dongle](https://www.amazon.com/TP-Link-wireless-network-Adapter-SoftAP/dp/B008IFXQFU/ref=sr_1_3?keywords=usb+wifi+adapter&qid=1582050405&sr=8-3)

## Before you start: hardware

1. Plug the USB webcam and the USB WiFi dongle into the Jetson Nano
2. Fit a jumper to J48 on the Jetson Nano board ([instructions](https://devtalk.nvidia.com/default/topic/1048640/jetson-nano/power-supply-considerations-for-jetson-nano-developer-kit/))
3. Flash the SD card, and you are good to go!

## Before you start: software

1. Register for an account at alwaysAI
2. Install alwaysAI CLI: `npm install --global alwaysai`

Before doing `balena push <app>` you need to download the models (too big to store at github). To do so run the following command: `ALWAYSAI_HOME=$(pwd) aai install` from the `chickenator` folder. It will download models and then fail at step `Install python virtual environment`, that is fine as long as the models were downloaded. 

## Usage: Visualization

To visualize a video stream:

- alwaysAI: http://deviceLocalIP:5000


## Usage: Change object detection model

You can change the model that is used to perform object detection via the `OBJECT_DETECTION_MODEL` environment variable:

| Neural Network Framework | Dataset | Model | OBJECT_DETECTION_MODEL value | Reference inference time |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| caffe | ILSVRC-2015 | SqueezeNet v1.1 SSD | squeezenet_v1.1 | 53 msec |
| caffe | ILSVRC-2010 | AlexNet | alexnet (default) | 83 msec |
| caffe | ILSVRC-2014 | GoogleNet | googlenet | 173 msec |
| tensorflow | ILSVRC-2014 | MobileNet v1 1.0_224 | mobilenet_v1_1.0_224 | 110 msec |

