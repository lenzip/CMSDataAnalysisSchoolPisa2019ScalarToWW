#!/bin/bash

# the mass for which you want to make the workspace
mass=$1 

#FIXME this is where the Combine framework is installed
cd /afs/cern.ch/work/l/lenzip/Combine_autoMC_May232018/CMSSW_8_1_0/
eval `scram runtime -sh`
cd -

workdir=`pwd`
datacarddir=`pwd`/datacardsInclusive

outputdir=`pwd`/combine
if [ ! -d "$outputdir" ]; then
  mkdir $outputdir
fi
  
cd $outputdir

#collect job output
combineTool.py -M Impacts -d workspace.${mass}.root -m ${mass} -t -1 --expectSignal=1 -o impacts.${mass}.nuis.json

rateparams=CMS_hww_WWnorm,CMS_hww_Topnorm,CMS_hww_DYttnorm,
combineTool.py -M Impacts -d workspace.${mass}.root -m ${mass} -t -1 --expectSignal=1 --named ${rateparams%?} -o impacts.${mass}.rateParams.json

#combine the two jsons
jq -s add impacts.${mass}.nuis.json impacts.${mass}.rateParams.json > impacts.${mass}.json
# make plots
plotImpacts.py -i impacts.${mass}.json -o impacts.${mass} 
