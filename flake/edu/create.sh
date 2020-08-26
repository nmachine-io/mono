#!/bin/bash

cd ./../app
img=gcr.io/nectar-bazaar/flake:latest
docker build . -t $img
docker push $img

cd ./../kerbi
img=gcr.io/nectar-bazaar/flake-tami:latest
docker build . -t $img
docker push $img