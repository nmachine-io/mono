#!/bin/bash

rm -rf /tmp/hub-wiz
rsync -r --exclude k8_kat --exclude wiz . /tmp/hub-wiz
rsync -r ~/workspace/k8-kat/k8_kat/. /tmp/hub-wiz/k8_kat
rsync -r ~/workspace/wiz/wiz/. /tmp/hub-wiz/wiz

docker build /tmp/hub-wiz -t hub-wizard -t gcr.io/nectar-bazaar/hub-wizard:latest
