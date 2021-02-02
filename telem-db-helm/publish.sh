#!/bin/bash
tag="$1"
local_image="telem-db"
public_image="us-central1-docker.pkg.dev/nectar-bazaar/public/$local_image"
docker build . -t "$local_image:$tag" -t "$public_image:$tag"
docker push "$public_image:$tag"