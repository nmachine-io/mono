#!/bin/bash
pipenv update
pipenv lock -r > requirements.txt
pip3 install -r requirements.txt