#!/bin/sh

#echo KILLING ALL SCRIPTS
sendmidi dev "Gestionnaire IAC Bus 1" cc 3 127    

osascript -e 'quit app "Live"'