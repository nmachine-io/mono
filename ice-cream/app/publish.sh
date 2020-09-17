#!/bin/bash

local_image="ice-cream-app"
public_img="gcr.io/nectar-bazaar/$local_image"
tag=$1

docker build . -t $public_img:$tag -t $local_image:$tag --build-arg VERSION=$tag
docker push $public_img:$tag