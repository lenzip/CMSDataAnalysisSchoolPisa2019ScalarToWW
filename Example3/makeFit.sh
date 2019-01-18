#!/bin/bash

# the mass for which you want to make the workspace
mass=$1 

#FIXME this is where the Combine framework is installed
cd /afs/cern.ch/work/l/lenzip/Combine_autoMC_May232018/CMSSW_8_1_0/
eval `scram runtime -sh`
cd -

workdir=`pwd`
datacarddir=`pwd`/datacardsJetBinned

outputdir=`pwd`/combine
if [ ! -d "$outputdir" ]; then
  mkdir $outputdir
fi
  
cd $outputdir

combine -M FitDiagnostics -t -1 --expectSignal=1 workspace.${mass}.root &> logFit.${mass}.txt
combine -M AsymptoticLimits -t -1 --expectSignal=0 workspace.${mass}.root &> logLimit.${mass}.txt
combine -M Significance -t -1 --expectSignal=1 workspace.${mass}.root &> logSignificance.${mass}.txt
