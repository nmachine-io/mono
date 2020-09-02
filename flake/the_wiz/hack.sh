#!/bin/bash
docker build . -t flake-wiz -t gcr.io/nectar-bazaar/flake-wiz
docker push gcr.io/nectar-bazaar/flake-wiz