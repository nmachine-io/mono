#!/bin/bash

chmod u+x "$PWD/local-eval.sh"
ln -sf "$PWD/local-eval.sh" /usr/local/bin/ice-cream-ktea-eval
ln -sf "$PWD/local-eval.sh" /usr/local/bin/ice-cream-ktea-eval:1.0.0

cd ./../kerbi-v2
chmod u+x "$PWD/local-eval.sh"
ln -sf "$PWD/local-eval.sh" /usr/local/bin/ice-cream-ktea-eval:2.0.0

cd ./../kerbi