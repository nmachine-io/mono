#!/bin/bash

KUBE_CONTEXT="selma"
NAMESPACE="ice-kream"
TMP_FILE=tmp_manifest.yaml

manifest=$(bundle exec ruby main.rb template $NAMESPACE \
  --set secrets.standard.db_creds.db_password="not-so-secure" \
  --set monolith.image="us-central1-docker.pkg.dev/nectar-bazaar/public/ice-kream-app:1.0.4" \
  --set monolith.service_type="LoadBalancer" \
)

echo "$manifest" > $TMP_FILE
kubectl create ns $NAMESPACE --context $KUBE_CONTEXT 2>/dev/null
kubectl apply -f tmp_manifest.yaml --context $KUBE_CONTEXT