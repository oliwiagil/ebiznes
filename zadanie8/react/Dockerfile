FROM ubuntu:22.04

ENV TZ=Europe/Warsaw \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y nodejs npm

EXPOSE 3000

RUN mkdir projekt
WORKDIR /usr/test/projekt/

RUN mkdir react

COPY . ./react

WORKDIR /usr/test/projekt/react/

CMD npm start