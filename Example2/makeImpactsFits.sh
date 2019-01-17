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

#do the initial fit
combineTool.py -M Impacts -d workspace.${mass}.root -m ${mass} --doInitialFit -t -1 --expectSignal=1 -n nuis 

# do the initial fit for rateParams separately
rateparams=CMS_hww_WWnorm,CMS_hww_Topnorm,CMS_hww_DYttnorm,
ranges=-2,4
rateparamsrange=${rateparams//,/=$ranges:}
combineTool.py -M Impacts -d workspace.${mass}.root -m ${mass} --doInitialFit -t -1 --expectSignal=1 --named ${rateparams%?} --setParameterRanges ${rateparamsrange%?} -n rateParams

# do the fits for each nuisance
combineTool.py -M Impacts -d workspace.${mass}.root -m ${mass} --doFits -t -1 --expectSignal=1 --job-mode condor --task-name nuis 

# do the fit for each rateParam
combineTool.py -M Impacts -d workspace.${mass}.root -m ${mass} --doFits -t -1 --expectSignal=1 --job-mode condor --task-name rateParams --named ${rateparams%?} --setParameterRanges ${rateparamsrange%?}
