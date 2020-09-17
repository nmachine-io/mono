#!/bin/bash

tag=$1

local_image="ice-cream-tami"
public_image="gcr.io/nectar-bazaar/$local_image"

docker build . -t $local_image:$tag -t $public_image:$tag --build-arg VERSION=$tag
docker push $public_image:$tag