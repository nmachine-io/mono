#!/bin/bash

nectwiz_version=$(awk -F== '{print $2}' <<< $(pipenv graph | grep nectwiz))
pub_image="gcr.io/nectar-bazaar/flake-wiz:$nectwiz_version"
docker build . -t flake-wiz -t $pub_image
docker push $pub_image