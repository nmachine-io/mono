#!/bin/bash
tag="$1"
local_image="tam"
public_image="us-central1-docker.pkg.dev/nectar-registry/nectar-ice-cream/$local_image"
docker build . -t "$local_image:$tag" -t "$public_image:$tag"
docker push "$public_image:$tag"
