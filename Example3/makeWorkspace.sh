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

combineCards.py SR0j=$datacarddir/hww2l2v_13TeV_0j/mTi/datacard.txt \
                SR1j=$datacarddir/hww2l2v_13TeV_1j/mTi/datacard.txt \
                SR2j=$datacarddir/hww2l2v_13TeV_2j/mTi/datacard.txt \
                SRvbf=$datacarddir/hww2l2v_13TeV_vbf/mTi/datacard.txt \
                TOP0j=$datacarddir/hww2l2v_13TeV_top_0j/events/datacard.txt \
                TOP1j=$datacarddir/hww2l2v_13TeV_top_1j/events/datacard.txt \
                TOP20j=$datacarddir/hww2l2v_13TeV_top_2j/events/datacard.txt \
                DY0j=$datacarddir/hww2l2v_13TeV_dytt_0j/events/datacard.txt \
                DY1j=$datacarddir/hww2l2v_13TeV_dytt_1j/events/datacard.txt \
                DY2j=$datacarddir/hww2l2v_13TeV_dytt_2j/events/datacard.txt \
                > combined.txt

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
                  --PO 'map=.*/ggH_hww_*:0' \
                  --PO 'map=.*/qqH_hww_*:0' \
                  --PO 'map=.*/ggH_hww_'${mass}':r[1,-10,10]' \
                  --PO 'map=.*/qqH_hww_'${mass}':r' \
                  combined.txt -o workspace.${mass}.root
