#!/bin/bash

chmod u+x "$PWD/local-eval.sh"
chmod u+x "$PWD/local-eval-v2.sh"

ln -s "$PWD/local-eval.sh" /usr/local/bin/ice-cream-tam-eval
ln -s "$PWD/local-eval-v2.sh" /usr/local/bin/ice-cream-tam-eval:2.0.0