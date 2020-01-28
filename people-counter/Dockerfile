FROM alwaysai/edgeiq:arm-latest
WORKDIR /usr/src

# Install alwaysAI CLI
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs
RUN npm install --global alwaysai

COPY . .
RUN pip install paho-mqtt
# Can't download models automatically since it requires auth
# RUN ALWAYSAI_HOME=$(pwd) aai app install; exit 0

CMD while : ; do echo "${MESSAGE=Idling...}"; sleep ${INTERVAL=600}; done
# CMD [ "python", "app.py" ]