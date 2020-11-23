#!/bin/bash

local_image="wiz-ci-tam"
public_image="gcr.io/nectar-bazaar/$local_image"

cd ./1.0.0
tag="1.0.0"
docker build . -t "$local_image:$tag" -t "$public_image:$tag"
docker push "$public_image:$tag"

cd ./../2.0.0
tag="2.0.0"
docker build . -t "$local_image:$tag" -t "$public_image:$tag"
docker push "$public_image:$tag"