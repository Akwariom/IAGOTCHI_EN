#!/bin/sh
echo Starting GoogleTrans
#export PYTHONPATH=$(dirname $0)/libs:$(dirname $0)/src/
cd $(dirname $0)/src
python3 -W ignore ./GoogleTrans.py
echo Done