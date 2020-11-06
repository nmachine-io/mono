#/bin/bash

sed -i -e "s/version: none"/"version: $1/g" values.yaml
