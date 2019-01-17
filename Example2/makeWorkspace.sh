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

combineCards.py SR=$datacarddir/hww2l2v_13TeV/mTi/datacard.txt \
                TOP=$datacarddir/hww2l2v_13TeV_top/events/datacard.txt \
                DY=$datacarddir/hww2l2v_13TeV_dytt/events/datacard.txt \
                > combined.txt

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
                  --PO 'map=.*/ggH_hww_*:0' \
                  --PO 'map=.*/qqH_hww_*:0' \
                  --PO 'map=.*/ggH_hww_'${mass}':r[1,-10,10]' \
                  --PO 'map=.*/qqH_hww_'${mass}':r' \
                  combined.txt -o workspace.${mass}.root
