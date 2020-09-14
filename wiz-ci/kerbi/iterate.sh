#!/bin/bash

image_common=gcr.io/nectar-bazaar/wiz-ci-tami

docker build . -f Dockerfile -t "$image_common:1.0.0"
docker build . -f Dockerfile-2.0.0 -t "$image_common:2.0.0"

docker push "$image_common:1.0.0"
docker push "$image_common:2.0.0"