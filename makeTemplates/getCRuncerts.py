#!/usr/bin/python

import os,sys,time,math

includeNB0 = False
discrim = 'minMlb'
templateYields = 'templates_'+discrim+'_noJSF_tau21Fix1_2016_10_8/lep80_MET100_NJets4_DR1_1jet200_2jet90/yields_'+discrim+'_2p318fb.txt' 
ttbarYields = '../makeCRs/ttbar_noJSF_notTag_tau21Fix1_2016_10_8/yields_'+discrim+'_2p318fb.txt'
wjetsYields = '../makeCRs/wjets_noJSF_notTag_tau21Fix1_2016_10_8/yields_'+discrim+'_2p318fb.txt'

lumiSys = 0.027 #lumi uncertainty
eltrigSys = 0.05 #electron trigger uncertainty
mutrigSys = 0.05 #muon trigger uncertainty
elIdSys = 0.01 #electron id uncertainty
muIdSys = 0.01 #muon id uncertainty
elIsoSys = 0.01 #electron isolation uncertainty
muIsoSys = 0.01 #muon isolation uncertainty

elcorrdSys = math.sqrt(lumiSys**2+eltrigSys**2+elIdSys**2+elIsoSys**2)
mucorrdSys = math.sqrt(lumiSys**2+mutrigSys**2+muIdSys**2+muIsoSys**2)

ftemplate = open(templateYields, 'rU')
templatelines = ftemplate.readlines()
ftemplate.close()
yields_top = {}
yields_ewk = {}
ind = 0
for line in templatelines:
	if 'Systematics' in line: break
	if line.startswith('top'): 
		for yld,cat in zip(line.split('&')[1:],templatelines[ind-1].split()[1:-1]):
			yields_top[cat] = float(yld.split()[0])
	if line.startswith('ewk'): 
		for yld,cat in zip(line.split('&')[1:],templatelines[ind-2].split()[1:-1]):
			yields_ewk[cat] = float(yld.split()[0])
	ind+=1
	
fttbar = open(ttbarYields, 'rU')
ttbarlines = fttbar.readlines()
fttbar.close()
dob_top = {}
ind = 0
for line in ttbarlines:
	if 'Systematics' in line: break
	if line.startswith('dataOverBkg'):
		for yld,cat in zip(line.split('&')[1:],ttbarlines[ind-6].split()[1:-1]):
			dob_top[cat] = float(yld.split()[0])
	ind+=1
	
fwjets = open(wjetsYields, 'rU')
wjetslines = fwjets.readlines()
fwjets.close()
dob_ewk = {}
ind = 0
for line in wjetslines:
	if 'Systematics' in line: break
	if line.startswith('dataOverBkg'): 
		for yld,cat in zip(line.split('&')[1:],wjetslines[ind-6].split()[1:-1]):
			dob_ewk[cat] = float(yld.split()[0])
	ind+=1
		
yields = {}
if includeNB0: yields['top_E_nB0']  = sum([yields_top[cat] for cat in yields_top.keys() if 'isE' in cat and cat.endswith('nB0')])
yields['top_E_nB1']  = sum([yields_top[cat] for cat in yields_top.keys() if 'isE' in cat and cat.endswith('nB1')])
yields['top_E_nB2p'] = sum([yields_top[cat] for cat in yields_top.keys() if 'isE' in cat and (cat.endswith('nB2') or cat.endswith('nB2p') or cat.endswith('nB3p'))])
yields['ewk_E_nW0']  = sum([yields_ewk[cat] for cat in yields_ewk.keys() if 'isE' in cat and 'nW0_' in cat])
yields['ewk_E_nW1p'] = sum([yields_ewk[cat] for cat in yields_ewk.keys() if 'isE' in cat and 'nW1p_' in cat])

if includeNB0: yields['top_M_nB0']  = sum([yields_top[cat] for cat in yields_top.keys() if 'isM' in cat and cat.endswith('nB0')])
yields['top_M_nB1']  = sum([yields_top[cat] for cat in yields_top.keys() if 'isM' in cat and cat.endswith('nB1')])
yields['top_M_nB2p'] = sum([yields_top[cat] for cat in yields_top.keys() if 'isM' in cat and (cat.endswith('nB2') or cat.endswith('nB2p') or cat.endswith('nB3p'))])
yields['ewk_M_nW0']  = sum([yields_ewk[cat] for cat in yields_ewk.keys() if 'isM' in cat and 'nW0_' in cat])
yields['ewk_M_nW1p'] = sum([yields_ewk[cat] for cat in yields_ewk.keys() if 'isM' in cat and 'nW1p_' in cat])

dataOverBkg = {}
if includeNB0: 
	dataOverBkg['top_E_nB0'] = abs(1-[dob_top[cat] for cat in dob_top.keys() if 'isE' in cat and cat.endswith('nB0')][0])
	dataOverBkg['top_M_nB0'] = abs(1-[dob_top[cat] for cat in dob_top.keys() if 'isM' in cat and cat.endswith('nB0')][0])
dataOverBkg['top_E_nB1'] = abs(1-[dob_top[cat] for cat in dob_top.keys() if 'isE' in cat and cat.endswith('nB1')][0])
dataOverBkg['top_M_nB1'] = abs(1-[dob_top[cat] for cat in dob_top.keys() if 'isM' in cat and cat.endswith('nB1')][0])
dataOverBkg['top_E_nB2p']= abs(1-[dob_top[cat] for cat in dob_top.keys() if 'isE' in cat and cat.endswith('nB2p')][0])
dataOverBkg['top_M_nB2p']= abs(1-[dob_top[cat] for cat in dob_top.keys() if 'isM' in cat and cat.endswith('nB2p')][0])

dataOverBkg['ewk_E_nW0'] = abs(1-[dob_ewk[cat] for cat in dob_ewk.keys() if 'isE' in cat and 'nW0_' in cat][0])
dataOverBkg['ewk_M_nW0'] = abs(1-[dob_ewk[cat] for cat in dob_ewk.keys() if 'isM' in cat and 'nW0_' in cat][0])
dataOverBkg['ewk_E_nW1p']= abs(1-[dob_ewk[cat] for cat in dob_ewk.keys() if 'isE' in cat and 'nW1p_' in cat][0])
dataOverBkg['ewk_M_nW1p']= abs(1-[dob_ewk[cat] for cat in dob_ewk.keys() if 'isM' in cat and 'nW1p_' in cat][0])

print "FULL CR:"
for key in sorted(yields.keys()):
	if '_M_' in key: continue
	print key.replace('E_',''),':',(yields[key]*dataOverBkg[key]+yields[key.replace('_E_','_M_')]*dataOverBkg[key.replace('_E_','_M_')])/(yields[key]+yields[key.replace('_E_','_M_')])
print

print "NORM SUBSTRACTED CR:"
for key in sorted(yields.keys()):
	if '_M_' in key: continue
	print key.replace('E_',''),':',math.sqrt(((yields[key]*dataOverBkg[key]+yields[key.replace('_E_','_M_')]*dataOverBkg[key.replace('_E_','_M_')])/(yields[key]+yields[key.replace('_E_','_M_')]))**2-((elcorrdSys*yields[key]+mucorrdSys*yields[key.replace('_E_','_M_')])/(yields[key]+yields[key.replace('_E_','_M_')]))**2)
print

ewk_isE=(yields['ewk_E_nW0']*dataOverBkg['ewk_E_nW0']+yields['ewk_E_nW1p']*dataOverBkg['ewk_E_nW1p'])/(yields['ewk_E_nW0']+yields['ewk_E_nW1p'])
ewk_isM=(yields['ewk_M_nW0']*dataOverBkg['ewk_M_nW0']+yields['ewk_M_nW1p']*dataOverBkg['ewk_M_nW1p'])/(yields['ewk_M_nW0']+yields['ewk_M_nW1p'])
ewk_all=((yields['ewk_E_nW0']+yields['ewk_E_nW1p'])*ewk_isE+(yields['ewk_M_nW0']+yields['ewk_M_nW1p'])*ewk_isM)/(yields['ewk_E_nW0']+yields['ewk_E_nW1p']+yields['ewk_M_nW0']+yields['ewk_M_nW1p'])
print 'ewk_isE :',ewk_isE
print 'ewk_isM :',ewk_isM 
print 'ewk_isL :',ewk_all
print

if includeNB0: 
	top_isE=(yields['top_E_nB0']*dataOverBkg['top_E_nB0']+yields['top_E_nB1']*dataOverBkg['top_E_nB1']+yields['top_E_nB2p']*dataOverBkg['top_E_nB2p'])/(yields['top_E_nB0']+yields['top_E_nB1']+yields['top_E_nB2p'])
	top_isM=(yields['top_M_nB0']*dataOverBkg['top_M_nB0']+yields['top_M_nB1']*dataOverBkg['top_M_nB1']+yields['top_M_nB2p']*dataOverBkg['top_M_nB2p'])/(yields['top_M_nB0']+yields['top_M_nB1']+yields['top_M_nB2p'])
	top_all=((yields['top_E_nB0']+yields['top_E_nB1']+yields['top_E_nB2p'])*top_isE+(yields['top_M_nB0']+yields['top_M_nB1']+yields['top_M_nB2p'])*top_isM)/(yields['top_E_nB0']+yields['top_E_nB1']+yields['top_E_nB2p']+yields['top_M_nB0']+yields['top_M_nB1']+yields['top_M_nB2p'])
else: 
	top_isE=(yields['top_E_nB1']*dataOverBkg['top_E_nB1']+yields['top_E_nB2p']*dataOverBkg['top_E_nB2p'])/(yields['top_E_nB1']+yields['top_E_nB2p'])
	top_isM=(yields['top_M_nB1']*dataOverBkg['top_M_nB1']+yields['top_M_nB2p']*dataOverBkg['top_M_nB2p'])/(yields['top_M_nB1']+yields['top_M_nB2p'])
	top_all=((yields['top_E_nB1']+yields['top_E_nB2p'])*top_isE+(yields['top_M_nB1']+yields['top_M_nB2p'])*top_isM)/(yields['top_E_nB1']+yields['top_E_nB2p']+yields['top_M_nB1']+yields['top_M_nB2p'])
print 'top_isE :',top_isE
print 'top_isM :',top_isM 
print 'top_isL :',top_all
