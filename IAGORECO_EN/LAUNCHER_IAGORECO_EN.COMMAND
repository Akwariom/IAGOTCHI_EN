#!/bin/sh
echo Starting Reco
#export PYTHONPATH=$(dirname $0)/libs:$(dirname $0)/src/
cd $(dirname $0)/src
python3 -W ignore ./asr_EN.py
echo Done