#!/bin/bash

pub_image="gcr.io/nectar-bazaar/flake-tami:latest"
docker build . -t flake-wiz -t $pub_image
docker push $pub_image