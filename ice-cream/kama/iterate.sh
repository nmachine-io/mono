#!/bin/bash
tag="${1:-1.0.0}"
pub_image="us-central1-docker.pkg.dev/nectar-bazaar/public/ice-cream-kama"
# pipenv update
docker build . -t "$pub_image:$tag"
docker push "$pub_image:$tag"
