FROM python:3.7.3-slim

RUN apt-get update && apt-get install -y python3-pip && apt-get install -y default-libmysqlclient-dev

# && apt-get install -y python3 && apt-get install -y python3-pip

ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/talkchapwebapi
WORKDIR /opt/talkchapwebapi
COPY . /opt/talkchapwebapi/
RUN pip3 install -r /opt/talkchapwebapi/requirements.txt
