import os,sys
import ROOT as rt

inputDir  = '/mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2018_Oct2019_4t_071420_step1hadds/nominal/'
rootfiles = os.popen('ls '+inputDir)

for file in rootfiles:
    if 'SingleElectron' in file: continue
    if 'SingleMuon' in file: continue
    if 'JetHT' in file: continue
    if 'EGamma' in file: continue
    RFile = rt.TFile(inputDir+file.strip(),'READ')
    hist1 = RFile.Get("NumTrueHist").Clone("NumTrueHist")
    hist2 = RFile.Get("weightHist").Clone("weightHist")
    print hist1.Integral(),hist2.GetBinContent(1),file.strip()
