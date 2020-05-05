#!/bin/bash

starting_point=$(pwd)

docker build $HOME/workspace/hub -t gcr.io/nectar-bazaar/hub-test:latest
docker push gcr.io/nectar-bazaar/hub-test:latest
kubectl delete persistentvolumeclaim -l app=hub --context cure
kubectl delete pod -l app=hub-test --context cure
kubectl delete deploy -l app=postgres --context cure

cd $HOME/workspace/charts-and-wizards/nectar-hub/kerbi-chart
ruby app.rb -e test > out.yaml
kubectl apply -f out.yaml

cd $starting_point

