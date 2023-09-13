#!/bin/sh
echo Starting Wiki
#export PYTHONPATH=$(dirname $0)/libs:$(dirname $0)/src/
cd $(dirname $0)/src
python3 -W ignore ./wiki.py
echo Done