#!/bin/bash

pub_image="gcr.io/nectar-bazaar/flake-tami:0.0.1"
docker build . -t flake-wiz -t $pub_image
docker push $pub_image