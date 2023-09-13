#!/bin/sh

cd $(dirname $0)

echo opening IAGORECO
open ../IAGORECO_EN/LAUNCHER_IAGORECO_EN.COMMAND &

sleep 2

echo opening IAGOBOT
open ../IAGOBOT_EN/LAUNCHER_IAGOBOT_EN.COMMAND &

sleep 2

echo opening IAGOWIKI
open ../IAGOWIKI_EN/LAUNCHER_IAGOWIKI_EN.COMMAND &

sleep 2

echo opening IAGOGENERATOR
open ../IAGOGENERATOR/LAUNCHER_IAGOGENERATOR.COMMAND &

sleep 2

echo opening IAGOTRANS FOR GENERATOR
open ../IAGOTRANS/LAUNCHER_IAGOTRANS.COMMAND &

sleep 2

#echo opening IAGOVOICE
#open -na "Ableton Live 9 Suite" ../../IAGOVOIX/iagoVoix.als &

echo opening IAGOGOTCHIPATCH
open ../IAGOPATCH_EN/IAGOTCHI_EN.maxpat &

sleep 30

echo opening ASR webpage
open -a "Google Chrome" 
open http://localhost:8080

sleep 30

echo opening IAGOCONSOLE
open ../IAGOCONSOLE/console/application.macosx/console.app &

echo Done
