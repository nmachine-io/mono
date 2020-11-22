#!/bin/bash
tag="$1"
local_image="ice-cream-tamsi"
public_image="gcr.io/nectar-bazaar/$local_image"
docker build . -f Dockerfile.tamsi -t "$local_image:$tag" -t "$public_image:$tag"
docker push "$public_image:$tag"