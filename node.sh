#!/usr/bin/env bash

java -Dwebdriver.chrome.driver="./chromedriver" \
    -Dwebdriver.gecko.driver="./geckodriver" \
    -jar selenium-server-standalone-3.12.0.jar \
    -role node \
    -hub http://127.0.0.1:4444/grid/register \
    -browser browserName=chrome,maxInstances=20 \
    -browser browserName=firefox,maxInstances=2
