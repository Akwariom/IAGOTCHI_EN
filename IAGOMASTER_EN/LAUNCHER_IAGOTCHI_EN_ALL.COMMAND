#!/bin/sh

#echo KILLING ALL SCRIPTS

cd $(dirname $0)

echo opening IAGORECO
open ../IAGORECO_EN/LAUNCHER_IAGORECO_EN.COMMAND &

echo opening IAGOBOT
open ../IAGOBOT_EN/LAUNCHER_IAGOBOT_EN.COMMAND &

echo opening IAGOWIKI
open ../IAGOWIKI_EN/LAUNCHER_IAGOWIKI_EN.COMMAND &

echo opening IAGOGENERATOR
open ../IAGOGENERATOR/LAUNCHER_IAGOGENERATOR.COMMAND &

echo opening IAGOTRANS FOR GENERATOR
open ../IAGOTRANS/LAUNCHER_IAGOTRANS.COMMAND &

echo opening IAGOVOICE
open ../../IAGOVOIX/iagoVoix.als &

echo opening IAGOGOTCHIPATCH
open ../IAGOPATCH_EN/IAGOTCHI_EN.maxpat &

sleep 1

echo opening ASR webpage
open http://localhost:8080

sleep 30

echo opening IAGOCONSOLE
open ../IAGOCONSOLE/console/application.macosx/console.app &

echo Done
