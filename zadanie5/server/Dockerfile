FROM ubuntu:22.04

ENV TZ=Europe/Warsaw \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y curl


EXPOSE 9000

RUN apt-get update &&\
    apt-get install openjdk-8-jdk -y

RUN mkdir /usr/test
WORKDIR /usr/test/

RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y unzip curl wget zip build-essential


RUN curl -s "https://get.sdkman.io" | bash
RUN chmod a+x "/root/.sdkman/bin/sdkman-init.sh"

RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install sbt 1.8.2"
RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install scala 2.12.17"

RUN mkdir projekt
WORKDIR /usr/test/projekt/

RUN mkdir server

COPY . ./server

ENV PATH=$PATH:/root/.sdkman/candidates/sbt/1.8.2/bin
ENV PATH=$PATH:/root/.sdkman/candidates/scala/2.12.17/bin

WORKDIR /usr/test/projekt/server/

CMD sbt run