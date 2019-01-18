# cuts

#supercut is applied to all other cuts  
supercut = 'mll>12  \
            && std_vector_lepton_pt[0]>25 && std_vector_lepton_pt[1]>10 \
            && std_vector_lepton_pt[2]<10 \
            && metPfType1 > 20 \
            && ptll > 30 \
            && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13) \
           '

# cuts are defined with a name and the selection

# DT->tautau control region
cuts['hww2l2v_13TeV_dytt_0j']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
                && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
                && ( mth<60) \
                && mll>40 && mll<80 \
                && std_vector_jet_pt[0] < 30 \
                '

cuts['hww2l2v_13TeV_dytt_1j']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
                && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
                && ( mth<60) \
                && mll>40 && mll<80 \
                && std_vector_jet_pt[0] > 30 \
                && std_vector_jet_pt[1] < 30 \
                '

cuts['hww2l2v_13TeV_dytt_2j']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
                && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
                && ( mth<60) \
                && mll>40 && mll<80 \
                && std_vector_jet_pt[1] > 30 \
                '

# top control region                
cuts['hww2l2v_13TeV_top_0j']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
                && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
                && mll>50 \
                && ( std_vector_jet_pt[0] > 20 ) \
                && ( std_vector_jet_pt[0] < 30 ) \
                && std_vector_jet_cmvav2[0]>-0.5884 \
                '

cuts['hww2l2v_13TeV_top_1j']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
                && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
                && mll>50 \
                && ( std_vector_jet_pt[0] > 30 ) \
                && ( std_vector_jet_pt[1] < 30 ) \
                && std_vector_jet_cmvav2[0]>-0.5884 \
                '

cuts['hww2l2v_13TeV_top_2j']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
                && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
                && mll>50 \
                && ( std_vector_jet_pt[1] > 30 ) \
                && std_vector_jet_cmvav2[0]>-0.5884 \
                && std_vector_jet_cmvav2[1]>-0.5884 \
                '
                
# signal region 
cuts['hww2l2v_13TeV_0j'] = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
                      && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
                      && mll>50 \
                      && std_vector_jet_pt[0] < 30 \
                      && '+bVeto+' \
                      '

cuts['hww2l2v_13TeV_1j'] = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
                      && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
                      && mll>50 \
                      && std_vector_jet_pt[0] > 30 \
                      && std_vector_jet_pt[1] < 30 \
                      && '+bVeto+' \
                      '

cuts['hww2l2v_13TeV_2j'] = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
                      && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
                      && mll>50 \
                      && std_vector_jet_pt[1] > 30 \
                      && (mjj < 400 || detajj < 3) \
                      && '+bVeto+' \
                      '

cuts['hww2l2v_13TeV_vbf'] = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
                      && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
                      && mll>50 \
                      && std_vector_jet_pt[1] > 30 \
                      && (mjj > 400 && detajj > 3) \
                      && '+bVeto+' \
                      '
                      
