#!/bin/bash

cd ./../app
img=gcr.io/nectar-bazaar/ice-cream:latest
docker build . -t $img
docker push $img

cd ./../kerbi
img=gcr.io/nectar-bazaar/ice-cream-tami:latest
docker build . -t $img
docker push $img