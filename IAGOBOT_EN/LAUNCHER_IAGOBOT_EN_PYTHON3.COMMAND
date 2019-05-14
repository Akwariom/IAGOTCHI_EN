#!/bin/sh
echo Starting ChatBot
export PYTHONPATH=$(dirname $0)/libs:$(dirname $0)/src/:$(dirname $0)/src/ChatterBot-blacklist
cd $(dirname $0)/src
python3 -W ignore ./IAGOBOT_EN.py
echo Done