#!/bin/bash

pub_image="gcr.io/nectar-bazaar/ice-cream-tami:latest"
docker build . -t ice-cream-wiz -t $pub_image
docker push $pub_image