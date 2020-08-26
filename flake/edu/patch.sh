#!/bin/bash


cd ./../

tag=1.0.1
img=gcr.io/nectar-bazaar/flake:$tag

echo "{\"version\": \"1.0.1\"}" > config.js

docker build . -t $img
docker push $img
nectl patch flake -n $tag -j "deployment.image=$img"