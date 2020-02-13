FROM alwaysai/edgeiq:nano-0.11.0
WORKDIR /usr/src

COPY . .
RUN pip3 install paho-mqtt

CMD [ "python3", "app.py" ]