FROM ubuntu:22.04

ENV TZ=Europe/Warsaw \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update &&\
	apt-get upgrade -y &&\
    apt-get install -y  build-essential unzip curl wget zip

EXPOSE 9000

RUN apt-get update -y && \
    apt-get install openjdk-8-jdk -y

RUN mkdir /usr/test
WORKDIR /usr/test/


RUN curl -s "https://get.sdkman.io" | bash
RUN chmod a+x "/root/.sdkman/bin/sdkman-init.sh"

RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install sbt 1.8.2"
RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install scala 2.12.17"

RUN mkdir projekt
WORKDIR /usr/test/projekt/

COPY ./zad2/ .

ENV PATH=$PATH:/root/.sdkman/candidates/sbt/1.8.2/bin
ENV PATH=$PATH:/root/.sdkman/candidates/scala/2.12.17/bin

WORKDIR /usr/test/
COPY ./script.sh .


RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
    tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
    echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
    tee /etc/apt/sources.list.d/ngrok.list && \
    apt update && apt install ngrok
  
RUN wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz --no-check-certificate
RUN tar -zxvf ngrok-v3-stable-linux-amd64.tgz
RUN mv ngrok /usr/bin/ngrok
RUN chmod 755 /usr/bin/ngrok

RUN ngrok config add-authtoken YOURS_AUTH_TOKEN


CMD /usr/test/script.sh







