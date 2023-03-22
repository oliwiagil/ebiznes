#!/bin/sh

cd /usr/test/projekt/
sbt run &
ngrok http 9000 --host-header="localhost:9000"