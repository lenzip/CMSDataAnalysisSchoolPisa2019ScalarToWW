
# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

nuisances['lumi']  = {
               'name'  : 'lumi_13TeV',
               'samples'  : {
                   #'DY'       : '1.025',    |
                   #'top'      : '1.025',    | These 3 backgrounds are data driven, no need to include the luminosity uncertainty
                   #'WW'       : '1.025',    |
                   'ggWW'     : '1.025',
                   'Vg'       : '1.025',
                   'VgS'      : '1.025',
                   'WZgS_L'   : '1.025',
                   'WZgS_H'   : '1.025',
                   'VZ'       : '1.025',
                   'VVV'      : '1.025',
                   'ggH_hww'  : '1.025',
                   'qqH_hww'  : '1.025',
                   'ZH_hww'   : '1.025',
                   'ggZH_hww' : '1.025',
                   'WH_hww'   : '1.025',
                   'bbH_hww'  : '1.025',
                   'ttH_hww'  : '1.025',
                   'ggH_htt'  : '1.025',
                   'qqH_htt'  : '1.025',
                   'ZH_htt'   : '1.025',
                   'WH_htt'   : '1.025',
                   'H_htt'    : '1.025',
                   },
               'type'  : 'lnN',
              }

massesFile = "masses.py"

if os.path.exists(massesFile) :
  handle = open(massesFile,'r')
  exec(handle)
  handle.close()
else:
  print "!!! ERROR file ", massesFile, " does not exist."

for m in masses:
  nuisances['lumi']['samples']['ggH_hww_'+m] = '1.025'
  nuisances['lumi']['samples']['qqH_hww_'+m] = '1.025'

#### FAKES

# already divided by central values in formulas !
fakeW_EleUp       = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp'
fakeW_EleDown     = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown'
fakeW_MuUp        = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp'
fakeW_MuDown      = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown'
fakeW_statEleUp   = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp'
fakeW_statEleDown = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown'
fakeW_statMuUp    = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp'
fakeW_statMuDown  = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown'

nuisances['fake_syst_em']  = {
               'name'  : 'CMS_hwwem_fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_em' : '1.30',
                             },
               }

nuisances['fake_syst_me']  = {
               'name'  : 'CMS_hwwme_fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_me' : '1.30',
                             },
               }

nuisances['fake_ele']  = {
                'name'  : 'hww_fake_ele',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_EleUp , fakeW_EleDown ],
                              'Fake_me'     : [ fakeW_EleUp , fakeW_EleDown ],
                             },
}

nuisances['fake_ele_stat']  = {
                'name'  : 'hww_fake_ele_stat',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                              'Fake_me'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                             },
}

nuisances['fake_mu']  = {
                'name'  : 'hww_fake_mu',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_MuUp , fakeW_MuDown ],
                              'Fake_me'     : [ fakeW_MuUp , fakeW_MuDown ],
                             },
}


nuisances['fake_mu_stat']  = {
                'name'  : 'hww_fake_mu_stat',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                              'Fake_me'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                             },
}

##### B-tagger

btagbc_syst = ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')']

nuisances['btagbc']  = {
                'name'  : 'btag_heavy',
                'kind'  : 'weight',
               'type'  : 'shape',
                'samples'  : {
                   'DY'      : btagbc_syst,
                   'WW'      : btagbc_syst,
                   'ggWW'    : btagbc_syst,
                   'VVV'     : btagbc_syst,
                   'VZ'      : btagbc_syst,
                   'WZgS_L'  : btagbc_syst,
                   'WZgS_H'  : btagbc_syst,
                   'top'     : btagbc_syst,
                   'Vg'      : btagbc_syst,
                   'VgS'     : btagbc_syst,
                   'ggH_hww' : btagbc_syst,
                   'qqH_hww' : btagbc_syst,
                   'WH_hww'  : btagbc_syst,
                   'ZH_hww'  : btagbc_syst,
                   'H_htt'   : btagbc_syst,
                   'bbH_hww' : btagbc_syst,
                   'ttH_hww' : btagbc_syst,
                   'ggH_htt' : btagbc_syst,  
                   'qqH_htt' : btagbc_syst,
                   'ZH_htt'  : btagbc_syst,
                   'WH_htt'  : btagbc_syst,
                }
}

for m in masses:
  nuisances['btagbc']['samples']['ggH_hww_'+m] = btagbc_syst
  nuisances['btagbc']['samples']['qqH_hww_'+m] = btagbc_syst


btagudsg_syst = ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')']

nuisances['btagudsg']  = {
                'name'  : 'btag_light',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : btagudsg_syst,
                   'VVV'     : btagudsg_syst,
                   'VZ'      : btagudsg_syst,
                   'WZgS_L'  : btagudsg_syst,
                   'WZgS_H'  : btagudsg_syst,
                   'WW'      : btagudsg_syst,
                   'ggWW'    : btagudsg_syst,
                   'top'     : btagudsg_syst,
                   'Vg'      : btagudsg_syst,
                   'VgS'     : btagudsg_syst,
                   'ggH_hww' : btagudsg_syst,
                   'qqH_hww' : btagudsg_syst,
                   'WH_hww'  : btagudsg_syst,
                   'ZH_hww'  : btagudsg_syst,
                   'bbH_hww' : btagudsg_syst,
                   'ttH_hww' : btagudsg_syst,
                   'H_htt'   : btagudsg_syst,
                   'ggH_htt' : btagudsg_syst,
                   'qqH_htt' : btagudsg_syst,
                   'ZH_htt'  : btagudsg_syst,
                   'WH_htt'  : btagudsg_syst,
                }
}
for m in masses:
  nuisances['btagudsg']['samples']['ggH_hww_'+m] = btagudsg_syst
  nuisances['btagudsg']['samples']['qqH_hww_'+m] = btagudsg_syst


##### Trigger Efficiency

trig_syst = ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)']

nuisances['trigg']  = {
                'name'  : 'hww_trigger',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : trig_syst ,
                   'VVV'     : trig_syst ,
                   'VZ'      : trig_syst ,
                   'WZgS_L'  : trig_syst ,
                   'WZgS_H'  : trig_syst ,
                   'ggWW'    : trig_syst ,
                   'WW'      : trig_syst ,
                   'top'     : trig_syst ,
                   'Vg'      : trig_syst ,
                   'VgS'     : trig_syst ,
                   'ggH_hww' : trig_syst ,
                   'qqH_hww' : trig_syst ,
                   'WH_hww'  : trig_syst ,
                   'ZH_hww'  : trig_syst ,
                   'ggZH_hww': trig_syst ,
                   'bbH_hww' : trig_syst ,
                   'ttH_hww' : trig_syst ,
                   'H_htt'   : trig_syst ,
                   'ggH_htt' : trig_syst ,
                   'qqH_htt' : trig_syst ,
                   'ZH_htt'  : trig_syst ,
                   'WH_htt'  : trig_syst ,
                },
}
for m in masses:
  nuisances['trigg']['samples']['ggH_hww_'+m] = trig_syst
  nuisances['trigg']['samples']['qqH_hww_'+m] = trig_syst

##### Electron Efficiency and energy scale

id_syst_ele = [ 'LepSF2l__ele_'+eleWP+'__Up' , 'LepSF2l__ele_'+eleWP+'__Do' ]

nuisances['eff_e']  = {
                'name'  : 'eff_e',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : id_syst_ele ,
                   'VVV'     : id_syst_ele ,
                   'VZ'      : id_syst_ele ,
                   'WZgS_L'  : id_syst_ele ,
                   'WZgS_H'  : id_syst_ele ,
                   'ggWW'    : id_syst_ele ,
                   'WW'      : id_syst_ele ,
                   'top'     : id_syst_ele ,
                   'Vg'      : id_syst_ele ,
                   'VgS'     : id_syst_ele ,
                   'ggH_hww' : id_syst_ele ,
                   'qqH_hww' : id_syst_ele ,
                   'WH_hww'  : id_syst_ele ,
                   'ZH_hww'  : id_syst_ele ,
                   'ggZH_hww': id_syst_ele ,
                   'bbH_hww' : id_syst_ele ,
                   'ttH_hww' : id_syst_ele ,
                   'H_htt'   : id_syst_ele ,
                   'ggH_htt' : id_syst_ele ,
                   'qqH_htt' : id_syst_ele ,
                   'ZH_htt'  : id_syst_ele ,
                   'WH_htt'  : id_syst_ele ,
                },
}
for m in masses:
  nuisances['eff_e']['samples']['ggH_hww_'+m] = id_syst_ele
  nuisances['eff_e']['samples']['qqH_hww_'+m] = id_syst_ele


##### Muon Efficiency and energy scale

id_syst_mu = [ 'LepSF2l__mu_'+muWP+'__Up' , 'LepSF2l__mu_'+muWP+'__Do' ]

nuisances['eff_m']  = {
                'name'  : 'eff_m',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : id_syst_mu ,
                   'VVV'     : id_syst_mu ,
                   'VZ'      : id_syst_mu ,
                   'WZgS_L'  : id_syst_mu ,
                   'WZgS_H'  : id_syst_mu ,
                   'ggWW'    : id_syst_mu ,
                   'WW'      : id_syst_mu ,
                   'top'     : id_syst_mu ,
                   'Vg'      : id_syst_mu ,
                   'VgS'     : id_syst_mu ,
                   'ggH_hww' : id_syst_mu ,
                   'qqH_hww' : id_syst_mu ,
                   'WH_hww'  : id_syst_mu ,
                   'ZH_hww'  : id_syst_mu ,
                   'ggZH_hww': id_syst_mu ,
                   'bbH_hww' : id_syst_mu ,
                   'ttH_hww' : id_syst_mu ,
                   'H_htt'   : id_syst_mu ,
                   'ggH_htt' : id_syst_mu ,
                   'qqH_htt' : id_syst_mu ,
                   'ZH_htt'  : id_syst_mu ,
                   'WH_htt'  : id_syst_mu ,
                },
}

for m in masses:
  nuisances['eff_m']['samples']['ggH_hww_'+m] = id_syst_mu
  nuisances['eff_m']['samples']['qqH_hww_'+m] = id_syst_mu


##### Jet energy scale

nuisances['jes']  = {
                'name'  : 'scale_j',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['1', '1'],
                   'ggWW'    : ['1', '1'],
                   'WW'      : ['1', '1'],
                   'top'     : ['1', '1'],
                   'VZ'      : ['1', '1'],
                   'WZgS_L'  : ['1', '1'],
                   'WZgS_H'  : ['1', '1'],
                   'VVV'     : ['1', '1'],
                   'Vg'      : ['1', '1'],
                   'VgS'     : ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww'  : ['1', '1'],
                   'ZH_hww'  : ['1', '1'],
                   'ggZH_hww': ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'ttH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                   'ggH_htt' : ['1', '1'] ,
                   'qqH_htt' : ['1', '1'] ,
                   'ZH_htt'  : ['1', '1'] ,
                   'WH_htt'  : ['1', '1'] ,
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__JESup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__JESdo'+skim,
}

for m in masses:
  nuisances['jes']['samples']['ggH_hww_'+m] = ['1', '1']
  nuisances['jes']['samples']['qqH_hww_'+m] = ['1', '1']

##### MET energy scale

nuisances['met']  = {
                'name'  : 'scale_met',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['1', '1'],
                   'ggWW'    : ['1', '1'],
                   'WW'      : ['1', '1'],
                   'top'     : ['1', '1'],
                   'VZ'      : ['1', '1'],
                   'WZgS_L'  : ['1', '1'],
                   'WZgS_H'  : ['1', '1'],
                   'VVV'     : ['1', '1'],
                   'Vg'      : ['1', '1'],
                   'VgS'     : ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww'  : ['1', '1'],
                   'ZH_hww'  : ['1', '1'],
                   'ggZH_hww': ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'ttH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                   'ggH_htt' : ['1', '1'] ,
                   'qqH_htt' : ['1', '1'] ,
                   'ZH_htt'  : ['1', '1'] ,
                   'WH_htt'  : ['1', '1'] ,
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__METup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__METdo'+skim,
}

for m in masses:
  nuisances['met']['samples']['ggH_hww_'+m] = ['1', '1']
  nuisances['met']['samples']['qqH_hww_'+m] = ['1', '1']


## Shape nuisance due to QCD scale variations for DY
nuisances['DYQCDscale']  = {
                'name'  : 'QCDscale_V',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['std_vector_LHE_weight[8]/std_vector_LHE_weight[0]', 'std_vector_LHE_weight[4]/std_vector_LHE_weight[0]'],
                }
}

nuisances['TopQCDscale']  = {
                'name'  : 'QCDscale_top',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'top'      : ['std_vector_LHE_weight[8]/std_vector_LHE_weight[0]', 'std_vector_LHE_weight[4]/std_vector_LHE_weight[0]'],
                }
}

nuisances['WWQCDscale']  = {
                'name'  : 'QCDscale_WW',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'      : ['std_vector_LHE_weight[8]/std_vector_LHE_weight[0]', 'std_vector_LHE_weight[4]/std_vector_LHE_weight[0]'],
                   'ggWW'    : ['std_vector_LHE_weight[8]/std_vector_LHE_weight[0]', 'std_vector_LHE_weight[4]/std_vector_LHE_weight[0]'],
                }
}

#  - WW shaping
nuisances['WWresum']  = {
                'name'  : 'WWresum',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                   },
                }


regions0j = ['hww2l2v_13TeV_dytt_0j', 'hww2l2v_13TeV_top_0j', 'hww2l2v_13TeV_0j']
regions1j = ['hww2l2v_13TeV_dytt_1j', 'hww2l2v_13TeV_top_1j', 'hww2l2v_13TeV_1j']
regions2j = ['hww2l2v_13TeV_dytt_2j', 'hww2l2v_13TeV_top_2j', 'hww2l2v_13TeV_2j', 'hww2l2v_13TeV_vbf']

nuisances['DYttnorm0j']  = {
               'name'  : 'CMS_hww_DYttnorm0j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts' : regions0j
              }

nuisances['WWnorm0j']  = {
               'name'  : 'CMS_hww_WWnorm0j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts' : regions0j
              }

nuisances['Topnorm0j']  = {
               'name'  : 'CMS_hww_Topnorm0j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts' : regions0j
              }

nuisances['DYttnorm1j']  = {
               'name'  : 'CMS_hww_DYttnorm1j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts' : regions1j
              }

nuisances['WWnorm1j']  = {
               'name'  : 'CMS_hww_WWnorm1j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts' : regions1j
              }

nuisances['Topnorm1j']  = {
               'name'  : 'CMS_hww_Topnorm1j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts' : regions1j
              }

nuisances['DYttnorm2j']  = {
               'name'  : 'CMS_hww_DYttnorm2j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts' : regions2j
              }

nuisances['WWnorm2j']  = {
               'name'  : 'CMS_hww_WWnorm2j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts' : regions2j
              }

nuisances['Topnorm2j']  = {
               'name'  : 'CMS_hww_Topnorm2j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts' : regions2j
              }


## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              'samples' : {}
             }

