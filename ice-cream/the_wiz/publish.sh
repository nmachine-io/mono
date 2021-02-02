#!/bin/bash
tag="${1:-1.0.0}"
pub_image="us-central1-docker.pkg.dev/nectar-registry/nectar-ice-cream/wiz"
docker build . -t "$pub_image:$tag"
docker push "$pub_image:$tag"
