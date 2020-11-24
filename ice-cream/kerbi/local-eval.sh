#!/bin/bash
cd "$(dirname "$(realpath "$BASH_SOURCE")")"
bundle exec ruby main.rb "$@"