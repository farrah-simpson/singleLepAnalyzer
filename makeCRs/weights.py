#!/usr/bin/python

targetlumi = 2318. # 1/pb

BR={}
BR['BW'] = 0.5
BR['TZ'] = 0.25
BR['TH'] = 0.25
BR['TTBWBW'] = BR['BW']*BR['BW']
BR['TTTHBW'] = 2*BR['TH']*BR['BW']
BR['TTTZBW'] = 2*BR['TZ']*BR['BW']
BR['TTTZTZ'] = BR['TZ']*BR['TZ']
BR['TTTZTH'] = 2*BR['TZ']*BR['TH']
BR['TTTHTH'] = BR['TH']*BR['TH']

BR['TW'] = 0.5
BR['BZ'] = 0.25
BR['BH'] = 0.25
BR['BBTWTW'] = BR['TW']*BR['TW']
BR['BBBHTW'] = 2*BR['BH']*BR['TW']
BR['BBBZTW'] = 2*BR['BZ']*BR['TW']
BR['BBBZBZ'] = BR['BZ']*BR['BZ']
BR['BBBZBH'] = 2*BR['BZ']*BR['BH']
BR['BBBHBH'] = BR['BH']*BR['BH']

# Number of processed MC events (before selections)
nRun={}
nRun['DY'] = 19259107. # from 28747969
nRun['TTJets'] = 14188545. # from 42784971
nRun['WJets'] = 16541248. # from 24184766
nRun['TTJetsPH'] = 96834559. # /TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2_ext3-v1/MINIAODSIM
nRun['TTJetsPH0to700inc'] = nRun['TTJetsPH']
nRun['TTJetsPH700to1000inc'] = nRun['TTJetsPH']*0.0921 + 3877762. #filtering efficiency coeff.
nRun['TTJetsPH1000toINFinc'] = nRun['TTJetsPH']*0.02474 + 2360497. #filtering efficiency coeff.
nRun['TTJetsPH700mtt'] = nRun['TTJetsPH']*0.0921 + 3877762.
nRun['TTJetsPH1000mtt'] = nRun['TTJetsPH']*0.02474 + 2360497.
nRun['WW'] = 993640. 
nRun['WZ'] = 978512.
nRun['ZZ'] = 996944.
nRun['TTWl'] = 129850. #from 252908
nRun['TTWq'] = 430330. #from 833964
nRun['TTZl'] = 184990. #from 398000
nRun['TTZq'] = 351398. #from 749800
nRun['WJetsMG100'] = 10142187.
nRun['WJetsMG200'] = 5231856.
nRun['WJetsMG400'] = 1901705.
nRun['WJetsMG600'] = 3984529.
nRun['WJetsMG800'] = 1574633.
nRun['WJetsMG1200'] = 255637.
nRun['WJetsMG2500'] = 253036.
nRun['Ts'] = 613384. #from 984400
nRun['Tt'] = 4291728. #from 19904330 (was 29892343 in miniAODv1)
nRun['TtW'] = 995600.
nRun['TbtW'] = 988500.
nRun['TTM700BWBW'] = 798600.0*0.333*0.333
nRun['TTM800BWBW'] = 822000.0*0.333*0.333
nRun['TTM900BWBW'] = 832800.0*0.333*0.333
nRun['TTM1000BWBW'] = 822800.0*0.333*0.333
nRun['TTM1100BWBW'] = 821600.0*0.333*0.333
nRun['TTM1200BWBW'] = 832800.0*0.333*0.333
nRun['TTM1300BWBW'] = 830400.0*0.333*0.333
nRun['TTM1400BWBW'] = 832800.0*0.333*0.333
nRun['TTM1500BWBW'] = 812200.0*0.333*0.333
nRun['TTM1600BWBW'] = 804000.0*0.333*0.333
nRun['TTM1700BWBW'] = 832400.0*0.333*0.333
nRun['TTM1800BWBW'] = 832800.0*0.333*0.333
nRun['TTM700THBW'] = 798600.0*0.333*0.333*2
nRun['TTM800THBW'] = 822000.0*0.333*0.333*2
nRun['TTM900THBW'] = 832800.0*0.333*0.333*2
nRun['TTM1000THBW'] = 822800.0*0.333*0.333*2
nRun['TTM1100THBW'] = 821600.0*0.333*0.333*2
nRun['TTM1200THBW'] = 832800.0*0.333*0.333*2
nRun['TTM1300THBW'] = 830400.0*0.333*0.333*2
nRun['TTM1400THBW'] = 832800.0*0.333*0.333*2
nRun['TTM1500THBW'] = 812200.0*0.333*0.333*2
nRun['TTM1600THBW'] = 804000.0*0.333*0.333*2
nRun['TTM1700THBW'] = 832400.0*0.333*0.333*2
nRun['TTM1800THBW'] = 832800.0*0.333*0.333*2
nRun['TTM700TZBW'] = 798600.0*0.333*0.333*2
nRun['TTM800TZBW'] = 822000.0*0.333*0.333*2
nRun['TTM900TZBW'] = 832800.0*0.333*0.333*2
nRun['TTM1000TZBW'] = 822800.0*0.333*0.333*2
nRun['TTM1100TZBW'] = 821600.0*0.333*0.333*2
nRun['TTM1200TZBW'] = 832800.0*0.333*0.333*2
nRun['TTM1300TZBW'] = 830400.0*0.333*0.333*2
nRun['TTM1400TZBW'] = 832800.0*0.333*0.333*2
nRun['TTM1500TZBW'] = 812200.0*0.333*0.333*2
nRun['TTM1600TZBW'] = 804000.0*0.333*0.333*2
nRun['TTM1700TZBW'] = 832400.0*0.333*0.333*2
nRun['TTM1800TZBW'] = 832800.0*0.333*0.333*2
nRun['TTM700TZTZ'] = 798600.0*0.333*0.333
nRun['TTM800TZTZ'] = 822000.0*0.333*0.333
nRun['TTM900TZTZ'] = 832800.0*0.333*0.333
nRun['TTM1000TZTZ'] = 822800.0*0.333*0.333
nRun['TTM1100TZTZ'] = 821600.0*0.333*0.333
nRun['TTM1200TZTZ'] = 832800.0*0.333*0.333
nRun['TTM1300TZTZ'] = 830400.0*0.333*0.333
nRun['TTM1400TZTZ'] = 832800.0*0.333*0.333
nRun['TTM1500TZTZ'] = 812200.0*0.333*0.333
nRun['TTM1600TZTZ'] = 804000.0*0.333*0.333
nRun['TTM1700TZTZ'] = 832400.0*0.333*0.333
nRun['TTM1800TZTZ'] = 832800.0*0.333*0.333
nRun['TTM700TZTH'] = 798600.0*0.333*0.333*2
nRun['TTM800TZTH'] = 822000.0*0.333*0.333*2
nRun['TTM900TZTH'] = 832800.0*0.333*0.333*2
nRun['TTM1000TZTH'] = 822800.0*0.333*0.333*2
nRun['TTM1100TZTH'] = 821600.0*0.333*0.333*2
nRun['TTM1200TZTH'] = 832800.0*0.333*0.333*2
nRun['TTM1300TZTH'] = 830400.0*0.333*0.333*2
nRun['TTM1400TZTH'] = 832800.0*0.333*0.333*2
nRun['TTM1500TZTH'] = 812200.0*0.333*0.333*2
nRun['TTM1600TZTH'] = 804000.0*0.333*0.333*2
nRun['TTM1700TZTH'] = 832400.0*0.333*0.333*2
nRun['TTM1800TZTH'] = 832800.0*0.333*0.333*2
nRun['TTM700THTH'] = 798600.0*0.333*0.333
nRun['TTM800THTH'] = 822000.0*0.333*0.333
nRun['TTM900THTH'] = 832800.0*0.333*0.333
nRun['TTM1000THTH'] = 822800.0*0.333*0.333
nRun['TTM1100THTH'] = 821600.0*0.333*0.333
nRun['TTM1200THTH'] = 832800.0*0.333*0.333
nRun['TTM1300THTH'] = 830400.0*0.333*0.333
nRun['TTM1400THTH'] = 832800.0*0.333*0.333
nRun['TTM1500THTH'] = 812200.0*0.333*0.333
nRun['TTM1600THTH'] = 804000.0*0.333*0.333
nRun['TTM1700THTH'] = 832400.0*0.333*0.333
nRun['TTM1800THTH'] = 832800.0*0.333*0.333
nRun['BBM700TWTW'] = 832200.0*0.333*0.333
nRun['BBM800TWTW'] = 818200.0*0.333*0.333
nRun['BBM900TWTW'] = 786200.0*0.333*0.333
nRun['BBM1000TWTW'] = 830800.0*0.333*0.333
nRun['BBM1100TWTW'] = 832900.0*0.333*0.333
nRun['BBM1200TWTW'] = 828600.0*0.333*0.333
nRun['BBM1300TWTW'] = 832800.0*0.333*0.333
nRun['BBM1400TWTW'] = 833000.0*0.333*0.333
nRun['BBM1500TWTW'] = 832600.0*0.333*0.333
nRun['BBM1600TWTW'] = 818200.0*0.333*0.333
nRun['BBM1700TWTW'] = 832800.0*0.333*0.333
nRun['BBM1800TWTW'] = 820800.0*0.333*0.333
nRun['BBM700BHTW'] = 832200.0*0.333*0.333*2
nRun['BBM800BHTW'] = 818200.0*0.333*0.333*2
nRun['BBM900BHTW'] = 786200.0*0.333*0.333*2
nRun['BBM1000BHTW'] = 830800.0*0.333*0.333*2
nRun['BBM1100BHTW'] = 832900.0*0.333*0.333*2
nRun['BBM1200BHTW'] = 828600.0*0.333*0.333*2
nRun['BBM1300BHTW'] = 832800.0*0.333*0.333*2
nRun['BBM1400BHTW'] = 833000.0*0.333*0.333*2
nRun['BBM1500BHTW'] = 832600.0*0.333*0.333*2
nRun['BBM1600BHTW'] = 818200.0*0.333*0.333*2
nRun['BBM1700BHTW'] = 832800.0*0.333*0.333*2
nRun['BBM1800BHTW'] = 820800.0*0.333*0.333*2
nRun['BBM700BZTW'] = 832200.0*0.333*0.333*2
nRun['BBM800BZTW'] = 818200.0*0.333*0.333*2
nRun['BBM900BZTW'] = 786200.0*0.333*0.333*2
nRun['BBM1000BZTW'] = 830800.0*0.333*0.333*2
nRun['BBM1100BZTW'] = 832900.0*0.333*0.333*2
nRun['BBM1200BZTW'] = 828600.0*0.333*0.333*2
nRun['BBM1300BZTW'] = 832800.0*0.333*0.333*2
nRun['BBM1400BZTW'] = 833000.0*0.333*0.333*2
nRun['BBM1500BZTW'] = 832600.0*0.333*0.333*2
nRun['BBM1600BZTW'] = 818200.0*0.333*0.333*2
nRun['BBM1700BZTW'] = 832800.0*0.333*0.333*2
nRun['BBM1800BZTW'] = 820800.0*0.333*0.333*2
nRun['BBM700BZBZ'] = 832200.0*0.333*0.333
nRun['BBM800BZBZ'] = 818200.0*0.333*0.333
nRun['BBM900BZBZ'] = 786200.0*0.333*0.333
nRun['BBM1000BZBZ'] = 830800.0*0.333*0.333
nRun['BBM1100BZBZ'] = 832900.0*0.333*0.333
nRun['BBM1200BZBZ'] = 828600.0*0.333*0.333
nRun['BBM1300BZBZ'] = 832800.0*0.333*0.333
nRun['BBM1400BZBZ'] = 833000.0*0.333*0.333
nRun['BBM1500BZBZ'] = 832600.0*0.333*0.333
nRun['BBM1600BZBZ'] = 818200.0*0.333*0.333
nRun['BBM1700BZBZ'] = 832800.0*0.333*0.333
nRun['BBM1800BZBZ'] = 820800.0*0.333*0.333
nRun['BBM700BZBH'] = 832200.0*0.333*0.333*2
nRun['BBM800BZBH'] = 818200.0*0.333*0.333*2
nRun['BBM900BZBH'] = 786200.0*0.333*0.333*2
nRun['BBM1000BZBH'] = 830800.0*0.333*0.333*2
nRun['BBM1100BZBH'] = 832900.0*0.333*0.333*2
nRun['BBM1200BZBH'] = 828600.0*0.333*0.333*2
nRun['BBM1300BZBH'] = 832800.0*0.333*0.333*2
nRun['BBM1400BZBH'] = 833000.0*0.333*0.333*2
nRun['BBM1500BZBH'] = 832600.0*0.333*0.333*2
nRun['BBM1600BZBH'] = 818200.0*0.333*0.333*2
nRun['BBM1700BZBH'] = 832800.0*0.333*0.333*2
nRun['BBM1800BZBH'] = 820800.0*0.333*0.333*2
nRun['BBM700BHBH'] = 832200.0*0.333*0.333
nRun['BBM800BHBH'] = 818200.0*0.333*0.333
nRun['BBM900BHBH'] = 786200.0*0.333*0.333
nRun['BBM1000BHBH'] = 830800.0*0.333*0.333
nRun['BBM1100BHBH'] = 832900.0*0.333*0.333
nRun['BBM1200BHBH'] = 828600.0*0.333*0.333
nRun['BBM1300BHBH'] = 832800.0*0.333*0.333
nRun['BBM1400BHBH'] = 833000.0*0.333*0.333
nRun['BBM1500BHBH'] = 832600.0*0.333*0.333
nRun['BBM1600BHBH'] = 818200.0*0.333*0.333
nRun['BBM1700BHBH'] = 832800.0*0.333*0.333
nRun['BBM1800BHBH'] = 820800.0*0.333*0.333
nRun['QCDht100'] = 81637494.
nRun['QCDht200'] = 18718905.
nRun['QCDht300'] = 19826197.
nRun['QCDht500'] = 19664159.
nRun['QCDht700'] = 15356448.
nRun['QCDht1000'] = 4963895.
nRun['QCDht1500'] = 3868886.
nRun['QCDht2000'] = 1912529.

#energy scale samples (Q^2)
nRun['TTJetsPHQ2U'] = 9921174.
nRun['TTJetsPHQ2D'] = 9860774.
nRun['TtWQ2U'] = 497600.
nRun['TtWQ2D'] = 499200.
nRun['TbtWQ2U'] = 500000.
nRun['TbtWQ2D'] = 497600.

# Cross sections for MC samples (in pb)
xsec={}
xsec['DY'] = 6025.2 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['TTJets'] = 831.76
xsec['WJets'] = 61526.7
xsec['TTJetsPH'] = 831.76 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['TTJetsPH0to700inc'] = 831.76
xsec['TTJetsPH700to1000inc'] = 831.76*0.0921 #(xsec*filtering coeff.)
xsec['TTJetsPH1000toINFinc'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['TTJetsPH700mtt'] = 831.76*0.0921 #(xsec*filtering coeff.)
xsec['TTJetsPH1000mtt'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['WJetsMG100'] = 1345.*1.21 # (1.21 = k-factor )# https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG200'] = 359.7*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG400'] = 48.91*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG600'] = 12.05*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG800'] = 5.501*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG1200'] = 1.329*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG2500'] = 0.03216*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns 
xsec['WW'] = 118.7 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeVInclusive
xsec['WZ'] = 47.13 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['ZZ'] = 16.523 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['TTZl'] = 0.2529 # from McM
xsec['TTZq'] = 0.5297 # from McM
xsec['TTWl'] = 0.2043 # from McM
xsec['TTWq'] = 0.4062 # from McM
xsec['Tt'] = 216.99/3 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['Ts'] = 11.36/3 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TtW'] = 35.6 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TbtW'] = 35.6 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma

xsec['TTM700']   = 0.455 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM800']  = 0.196 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM900']   = 0.0903 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1000']  = 0.0440 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1100']  = 0.0224 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1200'] = 0.0118 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1300']  = 0.00639 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1400'] = 0.00354 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1500']  = 0.00200 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1600'] = 0.001148 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1700']  = 0.000666 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1800'] = 0.000391 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo

xsec['BBM700']   = 0.455 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM800']  = 0.196 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM900']   = 0.0903 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1000']  = 0.0440 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1100']  = 0.0224 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1200'] = 0.0118 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1300']  = 0.00639 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1400'] = 0.00354 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1500']  = 0.00200 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1600'] = 0.001148 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1700']  = 0.000666 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1800'] = 0.000391 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo

xsec['QCDht100'] = 27990000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht200'] = 1712000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht300'] = 347700. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht500'] = 32100. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht700'] = 6831. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht1000'] = 1207. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht1500'] = 119.9 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht2000'] = 25.24 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD

#energy scale samples (Q^2)
xsec['TTJetsPHQ2U'] = xsec['TTJetsPH']
xsec['TTJetsPHQ2D'] = xsec['TTJetsPH']
xsec['TtWQ2U'] = xsec['TtW']
xsec['TtWQ2D'] = xsec['TtW']
xsec['TbtWQ2U'] = xsec['TbtW']
xsec['TbtWQ2D'] = xsec['TbtW']

# Calculate lumi normalization weights
weight = {}
weight['DY50'] = (targetlumi*xsec['DY']) / (nRun['DY'])
weight['TTJets'] = (targetlumi*xsec['TTJets']) / (nRun['TTJets'])
weight['WJets'] = (targetlumi*xsec['WJets']) / (nRun['WJets'])
weight['TTJetsPH'] = (targetlumi*xsec['TTJetsPH']) / (nRun['TTJetsPH'])
weight['TTJetsPH0to700inc'] = (targetlumi*xsec['TTJetsPH0to700inc']) / (nRun['TTJetsPH0to700inc'])
weight['TTJetsPH700to1000inc'] = (targetlumi*xsec['TTJetsPH700to1000inc']) / (nRun['TTJetsPH700to1000inc'])
weight['TTJetsPH1000toINFinc'] = (targetlumi*xsec['TTJetsPH1000toINFinc']) / (nRun['TTJetsPH1000toINFinc'])
weight['TTJetsPH700mtt'] = (targetlumi*xsec['TTJetsPH700mtt']) / (nRun['TTJetsPH700mtt'])
weight['TTJetsPH1000mtt'] = (targetlumi*xsec['TTJetsPH1000mtt']) / (nRun['TTJetsPH1000mtt'])
weight['WJetsMG100'] = (targetlumi*xsec['WJetsMG100']) / (nRun['WJetsMG100'])
weight['WJetsMG200'] = (targetlumi*xsec['WJetsMG200']) / (nRun['WJetsMG200'])
weight['WJetsMG400'] = (targetlumi*xsec['WJetsMG400']) / (nRun['WJetsMG400'])
weight['WJetsMG600'] = (targetlumi*xsec['WJetsMG600']) / (nRun['WJetsMG600'])
weight['WJetsMG800'] = (targetlumi*xsec['WJetsMG800']) / (nRun['WJetsMG800'])
weight['WJetsMG1200'] = (targetlumi*xsec['WJetsMG1200']) / (nRun['WJetsMG1200'])
weight['WJetsMG2500'] = (targetlumi*xsec['WJetsMG2500']) / (nRun['WJetsMG2500'])
weight['WW'] = (targetlumi*xsec['WW']) / (nRun['WW'])
weight['WZ'] = (targetlumi*xsec['WZ']) / (nRun['WZ'])
weight['ZZ'] = (targetlumi*xsec['ZZ']) / (nRun['ZZ'])
weight['TTWl'] = (targetlumi*xsec['TTWl']) / (nRun['TTWl'])
weight['TTWq'] = (targetlumi*xsec['TTWq']) / (nRun['TTWq'])
weight['TTZl'] = (targetlumi*xsec['TTZl']) / (nRun['TTZl'])
weight['TTZq'] = (targetlumi*xsec['TTZq']) / (nRun['TTZq'])
weight['Tt'] = (targetlumi*xsec['Tt']) / (nRun['Tt'])
weight['Ts'] = (targetlumi*xsec['Ts']) / (nRun['Ts'])
weight['TtW'] = (targetlumi*xsec['TtW']) / (nRun['TtW'])
weight['TbtW'] = (targetlumi*xsec['TbtW']) / (nRun['TbtW'])
weight['QCDht100'] = (targetlumi*xsec['QCDht100']) / (nRun['QCDht100'])
weight['QCDht200'] = (targetlumi*xsec['QCDht200']) / (nRun['QCDht200'])
weight['QCDht300'] = (targetlumi*xsec['QCDht300']) / (nRun['QCDht300'])
weight['QCDht500'] = (targetlumi*xsec['QCDht500']) / (nRun['QCDht500'])
weight['QCDht700'] = (targetlumi*xsec['QCDht700']) / (nRun['QCDht700'])
weight['QCDht1000'] = (targetlumi*xsec['QCDht1000']) / (nRun['QCDht1000'])
weight['QCDht1500'] = (targetlumi*xsec['QCDht1500']) / (nRun['QCDht1500'])
weight['QCDht2000'] = (targetlumi*xsec['QCDht2000']) / (nRun['QCDht2000'])
weight['TTM700BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM700']) / (nRun['TTM700BWBW'])
weight['TTM800BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM800']) / (nRun['TTM800BWBW'])
weight['TTM900BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM900']) / (nRun['TTM900BWBW'])
weight['TTM1000BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1000']) / (nRun['TTM1000BWBW'])
weight['TTM1100BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1100']) / (nRun['TTM1100BWBW'])
weight['TTM1200BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1200']) / (nRun['TTM1200BWBW'])
weight['TTM1300BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1300']) / (nRun['TTM1300BWBW'])
weight['TTM1400BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1400']) / (nRun['TTM1400BWBW'])
weight['TTM1500BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1500']) / (nRun['TTM1500BWBW'])
weight['TTM1600BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1600']) / (nRun['TTM1600BWBW'])
weight['TTM1700BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1700']) / (nRun['TTM1700BWBW'])
weight['TTM1800BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1800']) / (nRun['TTM1800BWBW'])
weight['TTM700THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM700']) / (nRun['TTM700THBW'])
weight['TTM800THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM800']) / (nRun['TTM800THBW'])
weight['TTM900THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM900']) / (nRun['TTM900THBW'])
weight['TTM1000THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1000']) / (nRun['TTM1000THBW'])
weight['TTM1100THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1100']) / (nRun['TTM1100THBW'])
weight['TTM1200THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1200']) / (nRun['TTM1200THBW'])
weight['TTM1300THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1300']) / (nRun['TTM1300THBW'])
weight['TTM1400THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1400']) / (nRun['TTM1400THBW'])
weight['TTM1500THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1500']) / (nRun['TTM1500THBW'])
weight['TTM1600THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1600']) / (nRun['TTM1600THBW'])
weight['TTM1700THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1700']) / (nRun['TTM1700THBW'])
weight['TTM1800THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1800']) / (nRun['TTM1800THBW'])
weight['TTM700TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM700']) / (nRun['TTM700TZBW'])
weight['TTM800TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM800']) / (nRun['TTM800TZBW'])
weight['TTM900TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM900']) / (nRun['TTM900TZBW'])
weight['TTM1000TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1000']) / (nRun['TTM1000TZBW'])
weight['TTM1100TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1100']) / (nRun['TTM1100TZBW'])
weight['TTM1200TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1200']) / (nRun['TTM1200TZBW'])
weight['TTM1300TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1300']) / (nRun['TTM1300TZBW'])
weight['TTM1400TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1400']) / (nRun['TTM1400TZBW'])
weight['TTM1500TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1500']) / (nRun['TTM1500TZBW'])
weight['TTM1600TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1600']) / (nRun['TTM1600TZBW'])
weight['TTM1700TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1700']) / (nRun['TTM1700TZBW'])
weight['TTM1800TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1800']) / (nRun['TTM1800TZBW'])
weight['TTM700TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM700']) / (nRun['TTM700TZTZ'])
weight['TTM800TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM800']) / (nRun['TTM800TZTZ'])
weight['TTM900TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM900']) / (nRun['TTM900TZTZ'])
weight['TTM1000TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1000']) / (nRun['TTM1000TZTZ'])
weight['TTM1100TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1100']) / (nRun['TTM1100TZTZ'])
weight['TTM1200TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1200']) / (nRun['TTM1200TZTZ'])
weight['TTM1300TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1300']) / (nRun['TTM1300TZTZ'])
weight['TTM1400TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1400']) / (nRun['TTM1400TZTZ'])
weight['TTM1500TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1500']) / (nRun['TTM1500TZTZ'])
weight['TTM1600TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1600']) / (nRun['TTM1600TZTZ'])
weight['TTM1700TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1700']) / (nRun['TTM1700TZTZ'])
weight['TTM1800TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1800']) / (nRun['TTM1800TZTZ'])
weight['TTM700TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM700']) / (nRun['TTM700TZTH'])
weight['TTM800TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM800']) / (nRun['TTM800TZTH'])
weight['TTM900TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM900']) / (nRun['TTM900TZTH'])
weight['TTM1000TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1000']) / (nRun['TTM1000TZTH'])
weight['TTM1100TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1100']) / (nRun['TTM1100TZTH'])
weight['TTM1200TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1200']) / (nRun['TTM1200TZTH'])
weight['TTM1300TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1300']) / (nRun['TTM1300TZTH'])
weight['TTM1400TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1400']) / (nRun['TTM1400TZTH'])
weight['TTM1500TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1500']) / (nRun['TTM1500TZTH'])
weight['TTM1600TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1600']) / (nRun['TTM1600TZTH'])
weight['TTM1700TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1700']) / (nRun['TTM1700TZTH'])
weight['TTM1800TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1800']) / (nRun['TTM1800TZTH'])
weight['TTM700THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM700']) / (nRun['TTM700THTH'])
weight['TTM800THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM800']) / (nRun['TTM800THTH'])
weight['TTM900THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM900']) / (nRun['TTM900THTH'])
weight['TTM1000THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1000']) / (nRun['TTM1000THTH'])
weight['TTM1100THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1100']) / (nRun['TTM1100THTH'])
weight['TTM1200THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1200']) / (nRun['TTM1200THTH'])
weight['TTM1300THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1300']) / (nRun['TTM1300THTH'])
weight['TTM1400THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1400']) / (nRun['TTM1400THTH'])
weight['TTM1500THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1500']) / (nRun['TTM1500THTH'])
weight['TTM1600THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1600']) / (nRun['TTM1600THTH'])
weight['TTM1700THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1700']) / (nRun['TTM1700THTH'])
weight['TTM1800THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1800']) / (nRun['TTM1800THTH'])
weight['BBM700TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM700']) / (nRun['BBM700TWTW'])
weight['BBM800TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM800']) / (nRun['BBM800TWTW'])
weight['BBM900TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM900']) / (nRun['BBM900TWTW'])
weight['BBM1000TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM1000']) / (nRun['BBM1000TWTW'])
weight['BBM1100TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM1100']) / (nRun['BBM1100TWTW'])
weight['BBM1200TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM1200']) / (nRun['BBM1200TWTW'])
weight['BBM1300TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM1300']) / (nRun['BBM1300TWTW'])
weight['BBM1400TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM1400']) / (nRun['BBM1400TWTW'])
weight['BBM1500TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM1500']) / (nRun['BBM1500TWTW'])
weight['BBM1600TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM1600']) / (nRun['BBM1600TWTW'])
weight['BBM1700TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM1700']) / (nRun['BBM1700TWTW'])
weight['BBM1800TWTW'] = (targetlumi*BR['BBTWTW']*xsec['BBM1800']) / (nRun['BBM1800TWTW'])
weight['BBM700BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM700']) / (nRun['BBM700BHTW'])
weight['BBM800BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM800']) / (nRun['BBM800BHTW'])
weight['BBM900BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM900']) / (nRun['BBM900BHTW'])
weight['BBM1000BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM1000']) / (nRun['BBM1000BHTW'])
weight['BBM1100BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM1100']) / (nRun['BBM1100BHTW'])
weight['BBM1200BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM1200']) / (nRun['BBM1200BHTW'])
weight['BBM1300BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM1300']) / (nRun['BBM1300BHTW'])
weight['BBM1400BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM1400']) / (nRun['BBM1400BHTW'])
weight['BBM1500BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM1500']) / (nRun['BBM1500BHTW'])
weight['BBM1600BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM1600']) / (nRun['BBM1600BHTW'])
weight['BBM1700BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM1700']) / (nRun['BBM1700BHTW'])
weight['BBM1800BHTW'] = (targetlumi*BR['BBBHTW']*xsec['BBM1800']) / (nRun['BBM1800BHTW'])
weight['BBM700BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM700']) / (nRun['BBM700BZTW'])
weight['BBM800BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM800']) / (nRun['BBM800BZTW'])
weight['BBM900BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM900']) / (nRun['BBM900BZTW'])
weight['BBM1000BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM1000']) / (nRun['BBM1000BZTW'])
weight['BBM1100BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM1100']) / (nRun['BBM1100BZTW'])
weight['BBM1200BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM1200']) / (nRun['BBM1200BZTW'])
weight['BBM1300BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM1300']) / (nRun['BBM1300BZTW'])
weight['BBM1400BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM1400']) / (nRun['BBM1400BZTW'])
weight['BBM1500BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM1500']) / (nRun['BBM1500BZTW'])
weight['BBM1600BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM1600']) / (nRun['BBM1600BZTW'])
weight['BBM1700BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM1700']) / (nRun['BBM1700BZTW'])
weight['BBM1800BZTW'] = (targetlumi*BR['BBBZTW']*xsec['BBM1800']) / (nRun['BBM1800BZTW'])
weight['BBM700BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM700']) / (nRun['BBM700BZBZ'])
weight['BBM800BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM800']) / (nRun['BBM800BZBZ'])
weight['BBM900BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM900']) / (nRun['BBM900BZBZ'])
weight['BBM1000BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM1000']) / (nRun['BBM1000BZBZ'])
weight['BBM1100BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM1100']) / (nRun['BBM1100BZBZ'])
weight['BBM1200BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM1200']) / (nRun['BBM1200BZBZ'])
weight['BBM1300BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM1300']) / (nRun['BBM1300BZBZ'])
weight['BBM1400BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM1400']) / (nRun['BBM1400BZBZ'])
weight['BBM1500BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM1500']) / (nRun['BBM1500BZBZ'])
weight['BBM1600BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM1600']) / (nRun['BBM1600BZBZ'])
weight['BBM1700BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM1700']) / (nRun['BBM1700BZBZ'])
weight['BBM1800BZBZ'] = (targetlumi*BR['BBBZBZ']*xsec['BBM1800']) / (nRun['BBM1800BZBZ'])
weight['BBM700BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM700']) / (nRun['BBM700BZBH'])
weight['BBM800BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM800']) / (nRun['BBM800BZBH'])
weight['BBM900BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM900']) / (nRun['BBM900BZBH'])
weight['BBM1000BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM1000']) / (nRun['BBM1000BZBH'])
weight['BBM1100BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM1100']) / (nRun['BBM1100BZBH'])
weight['BBM1200BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM1200']) / (nRun['BBM1200BZBH'])
weight['BBM1300BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM1300']) / (nRun['BBM1300BZBH'])
weight['BBM1400BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM1400']) / (nRun['BBM1400BZBH'])
weight['BBM1500BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM1500']) / (nRun['BBM1500BZBH'])
weight['BBM1600BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM1600']) / (nRun['BBM1600BZBH'])
weight['BBM1700BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM1700']) / (nRun['BBM1700BZBH'])
weight['BBM1800BZBH'] = (targetlumi*BR['BBBZBH']*xsec['BBM1800']) / (nRun['BBM1800BZBH'])
weight['BBM700BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM700']) / (nRun['BBM700BHBH'])
weight['BBM800BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM800']) / (nRun['BBM800BHBH'])
weight['BBM900BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM900']) / (nRun['BBM900BHBH'])
weight['BBM1000BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM1000']) / (nRun['BBM1000BHBH'])
weight['BBM1100BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM1100']) / (nRun['BBM1100BHBH'])
weight['BBM1200BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM1200']) / (nRun['BBM1200BHBH'])
weight['BBM1300BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM1300']) / (nRun['BBM1300BHBH'])
weight['BBM1400BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM1400']) / (nRun['BBM1400BHBH'])
weight['BBM1500BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM1500']) / (nRun['BBM1500BHBH'])
weight['BBM1600BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM1600']) / (nRun['BBM1600BHBH'])
weight['BBM1700BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM1700']) / (nRun['BBM1700BHBH'])
weight['BBM1800BHBH'] = (targetlumi*BR['BBBHBH']*xsec['BBM1800']) / (nRun['BBM1800BHBH'])

#energy scale samples (Q^2)
weight['TTJetsPHQ2U'] = (targetlumi*xsec['TTJetsPHQ2U']) / (nRun['TTJetsPHQ2U'])
weight['TTJetsPHQ2D'] = (targetlumi*xsec['TTJetsPHQ2D']) / (nRun['TTJetsPHQ2D'])
weight['TtWQ2U'] = (targetlumi*xsec['TtWQ2U']) / (nRun['TtWQ2U'])
weight['TtWQ2D'] = (targetlumi*xsec['TtWQ2D']) / (nRun['TtWQ2D'])
weight['TbtWQ2U'] = (targetlumi*xsec['TbtWQ2U']) / (nRun['TbtWQ2U'])
weight['TbtWQ2D'] = (targetlumi*xsec['TbtWQ2D']) / (nRun['TbtWQ2D'])

