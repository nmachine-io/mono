#!/bin/bash

#pipenv update
#nectwiz_version=$(awk -F== '{print $2}' <<< $(pipenv graph | grep nectwiz))
nectwiz_version='latest'
pub_image="gcr.io/nectar-bazaar/flake-wiz:$nectwiz_version"
docker build . -t flake-wiz -t $pub_image
docker push $pub_image