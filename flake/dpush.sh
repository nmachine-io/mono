#!/bin/bash
img=gcr.io/nectar-bazaar/flake
docker build $HOME/workspace/nectarines/flake/app -t $img
docker push $img