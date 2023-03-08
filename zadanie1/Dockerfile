FROM ubuntu:22.04

ENV TZ=Europe/Warsaw \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install libssl-dev openssl wget gcc make \
    build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev \
    unzip -y

RUN wget https://www.python.org/ftp/python/3.8.16/Python-3.8.16.tgz && \
    tar xzf Python-3.8.16.tgz && \
    cd Python-3.8.16 && \
    ./configure --prefix=/usr/local && \
    make && \
    make install

RUN apt-get update -y && \
    apt-get install openjdk-8-jdk -y

RUN apt-get update -y && \
    apt-get install kotlin -y

RUN wget https://services.gradle.org/distributions/gradle-8.0.2-bin.zip && \
    mkdir /opt/gradle && \
    unzip -d /opt/gradle gradle-8.0.2-bin.zip
    
ENV PATH=$PATH:/opt/gradle/gradle-8.0.2/bin

RUN mkdir /usr/test
WORKDIR /usr/test
RUN gradle init --type java-application --dsl groovy --project-name test --test-framework junit-jupiter  --incubating --package test

COPY build.gradle /usr/test/app/
RUN gradle

CMD gradle run







