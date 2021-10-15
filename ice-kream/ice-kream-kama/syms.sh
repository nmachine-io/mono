#!/bin/bash

if [ "$1" == "create" ]
then
  echo "creating"
  ln -s "$HOME/workspace/kama-sdk-py/kama_sdk" kama_sdk
  ln -s "$HOME/workspace/mono/prom-plugin/prom-plugin-kama/kama_prom_plugin" kama_prom_plugin
  ln -s "$HOME/workspace/mono/telem-plugin/telem-plugin-kama/kama_telem_plugin" kama_telem_plugin
elif [ "$1" == "delete" ]
then
  echo "deleting"
  rm kama_sdk
  rm kama_prom_plugin
  rm kama_telem_plugin
else
  echo "Unrecognized command '$1'"
fi