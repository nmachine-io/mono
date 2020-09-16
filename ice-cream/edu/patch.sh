#!/bin/bash


cd ./../

tag=1.0.1
img=gcr.io/nectar-bazaar/ice-cream:$tag

echo "{\"version\": \"1.0.1\"}" > config.js

docker build . -t $img
docker push $img
nectl patch ice-cream -n $tag -j "deployment.image=$img"