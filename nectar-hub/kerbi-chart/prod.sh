#!/bin/bash

starting_point=$(pwd)

docker build $HOME/workspace/hub -t gcr.io/nectar-bazaar/hub:latest
docker push gcr.io/nectar-bazaar/hub:latest

docker build $HOME/workspace/hub-front -t gcr.io/nectar-bazaar/hub-front:latest
docker push gcr.io/nectar-bazaar/hub-front:latest

#kubectl delete secret --all -n hub
kubectl delete deploy -l app=hub -n hub
#kubectl delete deploy -l app=postgres -n hub
kubectl delete deploy -l app=hub-front -n hub

cd $HOME/workspace/charts-and-wizards/nectar-hub/kerbi-chart
ruby app.rb -e production > out.yaml
kubectl apply -f out.yaml

cd $starting_point