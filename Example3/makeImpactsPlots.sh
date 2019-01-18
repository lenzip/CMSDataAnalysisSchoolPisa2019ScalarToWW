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
combineTool.py -M Impacts -d workspace.${mass}.root -m ${mass} -t -1 --expectSignal=1 -o impacts.${mass}.nuis.json -n nuis.${mass}

rateparams=CMS_hww_WWnorm0j,CMS_hww_Topnorm0j,CMS_hww_DYttnorm0j,CMS_hww_WWnorm1j,CMS_hww_Topnorm1j,CMS_hww_DYttnorm1j,CMS_hww_WWnorm2j,CMS_hww_Topnorm2j,CMS_hww_DYttnorm2j,
combineTool.py -M Impacts -d workspace.${mass}.root -m ${mass} -t -1 --expectSignal=1 --named ${rateparams%?} -o impacts.${mass}.rateParams.json -n rateParams.${mass}

#combine the two jsons
echo "{\"params\":" > impacts.${mass}.json
jq -s ".[0].params+.[1].params" impacts.${mass}.nuis.json impacts.${mass}.rateParams.json >> impacts.${mass}.json 
echo ",\"POIs\":" >> impacts.${mass}.json
jq -s ".[0].POIs" impacts.${mass}.nuis.json impacts.${mass}.rateParams.json >> impacts.${mass}.json
echo "}" >> impacts.${mass}.json
# make plots
plotImpacts.py -i impacts.${mass}.json -o impacts.${mass} 
