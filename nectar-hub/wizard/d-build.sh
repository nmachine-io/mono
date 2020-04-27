#!/bin/bash

rsync -r --exclude k8_kat --exclude wiz . /tmp/hub-wiz
rsync -r ~/workspace/k8-kat/k8_kat/. /tmp/hub-wiz/k8_kat/.
rsync -r ~/workspace/k8-kat/wiz/. /tmp/hub-wiz/wiz/.

docker build /tmp/hub-wiz -t hub-wizard