#!/bin/bash

tag=$1

local_image="telem-tami"
public_image="gcr.io/nectar-bazaar/$local_image"

docker build . -t $local_image:$tag -t $public_image:$tag
docker push $public_image:$tag
