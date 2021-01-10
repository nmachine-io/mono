#!/bin/bash
cd "$(dirname "$(realpath "$BASH_SOURCE")")"
bundle exec ruby main-v2.rb "$@" -f values-v2.yaml