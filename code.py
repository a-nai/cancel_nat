import time
import numpy as np
import pickle

drugs2= pickle.load(open("drugs2.pkl","rb"));
cancelmol = pickle.load(open("cancelmol.pkl","rb"));

molecules=['Apigenin', 'Chaetocin', 'Chrysin', 'Curcumin', 'Epigallocatechin gallate (EGCG)', 'Luteolin', 'Myricetin', 'Quercetin', 'Resveratrol', 'Wogonin', 'Brusatol', 'Piperlongumine', 'Trigonelline', 'Pentyl isothiocyanate (PEITC)', 'Pleurotin', 'Plumbagin', 'EM23', 'Parthenolid', 'Sulforaphane', 'Melatonin']

import csv
drugA=[];
with open('/Users/andrejeremcuk/Downloads/DrugAge Browse (1).csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
       print(row);drugA.append(row)  #//print(', '.join(row))

len(drugA)
drugA[1:5]
drugAb=[]
for i in range(1,len(drugA)): 
 drugAb.append(str(drugA[i][0].split(',')[0]).replace('"', '')) 



s=[];
t=drugAb
for i in t:
       if i not in s:
          s.append(i)


drugA=s;



def forfer(l,drug7):
     ii0='no';
     t1=l.find(drug7);
     if t1==-1: return 'no';
     t2=l.find('apoptosis');
     t4=l.find('Inhibition of cancer');
     t5=l.find('cancer');
     #t6=re.search('autophagy',fer[u],re.IGNORECASE);
     t6=l.find('autophagy');
     if t6!=None: print(t6,u);
     t7=l.find('Autophagy');
     t8=l.find('anticancer');
     t9=l.find('antiproliferative');
     t10=l.find('apoptotic');
     t11=l.find('Inhibits Cancer Metastasis');
     t12=l.find('Angiogenesis');
     t13=l.find('cytotoxicity');
     t14=l.find('anti-tumor');
     t15=l.find('anticancer therapy');
     t16=l.find('antitumor');
     t17=l.find('inhibits');
     t5=l.find('cancer');
     t18=l.find('cancer growth');
     t19=l.find('cancer therapy');
     t20=l.find('antiangiogenic');
     t21=l.find('anti-cancer');
     if (t21!=-1)or(t20!=-1)or(t19!=-1)or(t18!=-1)or(t17!=-1)or(t16!=-1)or(t15!=-1)or(t14!=-1)or(t13!=-1)or(t12!=-1)or(t11!=-1)or(t10!=-1)or(t9!=-1)or(t8!=-1)or(t7!=-1)or(t6!=-1)or(t4!=-1)or(t2!=-1): return 'yes';
     else: return 'no';

def ferfor(l,drug7):
     t1=l.find(drug7);
     t2=l.find('accelerate');
     t4=l.find('promotes');
     t6=l.find('Stimulates');
     t7=l.find('Metastasis');
     t5=l.find('cancer');
     t8=l.find('promote');
     t9=l.find('tumorigenesis');
     t10=l.find('metastasis');
     t11=l.find('stimulates');
     if ((t11!=-1)or(t10!=-1)or(t9!=-1)or(t8!=-1)or(t7!=-1)or(t6!=-1)or(t4!=-1)or(t2!=-1))and(t1!=-1): return 'yes';
     else: return 'no';
     
     
for u in range(len(drugA)):#len(drugA)
 MAX_COUNT = 400;
 TERM=drugA[u] +' cancer';print(drugA[u],u);ii7.append(('it',drugA[u],u));ii6.append(('it',drugA[u],u))
 try: h=Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
 except: time.sleep(5);print('error',u);h=Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
 result = Entrez.read(h)
 ids = result['IdList']
 h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
 ret = Medline.parse(h)
 fer=[];
 for re in ret:
  try: tr=re['TI'];
  except: tr='0';
  fer.append(tr);
 for m in range(len(fer)):
  i=drugA[u].find(' ');
  if i!=-1: i7=forfer(fer[m],drugA[u][:i]);
  s=drugA[u];
  i8=forfer(fer[m],s);
  s=s[0].lower()+s[1:];
  i9=forfer(fer[m],s);
  i6=forfer(fer[m],s);
  if i6=='yes': ii6.append((fer[m],drugA[u]));
  if (i9=='yes')or(i8=='yes')or(i7=='yes'): ii7.append((fer[m],drugA[u]));


     
    
iii7=[];

for u in range(len(s)):#len(drugA)
 iii7.append(('it',s[u],u));
 for h in range(len(cancers)):#len(drugA)
  MAX_COUNT = 400;
  TERM=s[u] +' '+cancers[h];print(s[u],u);#iii7.append(('it',s[u],u));
  try: hi=Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
  except: time.sleep(5);print('error',u);hi=Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
  result = Entrez.read(hi)
  ids = result['IdList']
  hi = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
  ret = Medline.parse(hi)
  fer=[];
  for re1 in ret:
   try: tr=re1['TI'];
   except: tr='0';
   fer.append(tr);
  for m in range(len(fer)):
   if (re.search(cancers[h],fer[m],re.IGNORECASE))and(re.search(s[u],fer[m],re.IGNORECASE)): iii7.append((fer[m],s[u],cancers[h]));



cancers=['Liver Cancer', 'Thyroid Cancer', 'Pancreatic Cancer', 'Leukemia', 'Kidney Cancer', 'Non-Hodgkins Lymphoma', 'Bladder Cancer', 'Melanoma', 'Colonorectal Cancers', 'Prostate Cancer', 'Lung Cancer', 'Breast Cancer', 'squamous cell carcinoma', 'gastric cancer'];


ii=[];


for u in range(len(cancers)): #len(cancers)
 MAX_COUNT = 7000;print(u);
 TERM=cancers[u]+' gene';jj.append(('it',cancers[u],len(ii),'end'))
 try: h=Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
 except IncompleteRead: continue
 result = Entrez.read(h)
 ids = result['IdList']
 h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
 ret = Medline.parse(h)
 fer=[];
 for re in ret:
  try: tr=re['TI'];
  except: tr='0';
  fer.append(tr);
 for m in range(len(fer)):
  ii0='no';
  for j in range(len(ma00pp)):
   if (ma00pp[j]!=0): ii0=forf(fer[m],ma00pp[j])
   if ii0=='yes': ii.append((fer[m],ma00pp[j],cancers[u]))


output = open('ii.pkl', 'wb')
pickle.dump(ii, output)
output.close()



cancersgene = pickle.load(open("cancersgene.pkl","rb"));

import re
import numpy

i7cm=[[] for i in range(len(cancelmol))];
for u in range(len(cancelmol)):#len(drugA)
 MAX_COUNT = 400;
 TERM=cancelmol[u] +' gene';print(cancelmol[u],u);#ii7.append(('it',drugA[u],u));ii6.append(('it',drugA[u],u))
 try: h=Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
 except: time.sleep(5);print('error',u);h=Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
 result = Entrez.read(h)
 ids = result['IdList']
 h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
 ret = Medline.parse(h)
 fer=[];
 for r in ret:
  try: tr=r['TI'];
  except: tr='0';
  fer.append(tr);
 for m in range(len(fer)):
  for j in range(1,len(ma00pp)):
   if ma00pp[j]!=0:
    if (re.search(cancelmol[u],fer[m]))and(re.search(ma00pp[j],fer[m])):
     i7cm[u].append((fer[m],cancelmol[u],ma00pp[j]));



i8cm=[[] for i in range(len(cancelmol))];
for u in range(len(cancelmol)):#len(drugA)
 for k in range(len(cancers)):
  MAX_COUNT = 100;
  TERM=cancelmol[u] +' '+ cancers[k];print(cancelmol[u],u,cancers[k]);#ii7.append(('it',drugA[u],u));ii6.append(('it',drugA[u],u))
  try: h=Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
  except: time.sleep(5);print('error',u);h=Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
  result = Entrez.read(h)
  ids = result['IdList']
  h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
  ret = Medline.parse(h)
  fer=[];
  for r in ret:
   try: tr=r['TI'];
   except: tr='0';
   fer.append(tr);
  for m in range(len(fer)):
   if (re.search(cancelmol[u],fer[m]))and(re.search(cancers[k],fer[m])):
    i8cm[u].append((fer[m],cancelmol[u],cancers[k]));


i9cm=[0 for i in range(len(cancelmol))];
for u in range(len(cancelmol)):
 for k in range(len(i8cm[u])):
  i9cm[u]+=5;
 for k in range(len(i7cm[u])):
  i9cm[u]+=1;

s9=numpy.argsort(i9cm)


for u in range(1,len(cancelmol)):
 print(cancelmol[s9[-u]],u)

for u in range(len(drugs2)):
 print(drugs2[u],u)

i8cm = pickle.load(open("i8cm.pkl","rb"));

i7cm = pickle.load(open("i7cm.pkl","rb"));

ma00pp = pickle.load(open("ma00pp.pkl","rb"));

output = open('i8cm.pkl', 'wb')
pickle.dump(i8cm, output)
output.close()
output = open('i7cm.pkl', 'wb')
pickle.dump(i7cm, output)
output.close()


b9=0;
for u in range(len(cancelmol)):
 if i8cm[u]==[]: b9+=1;


b9=0;
for u in range(len(cancelmol)):
 if i7cm[u]==[]: b9+=1;



for k in range(len(cancersgene)): print(len(cancersgene[k]))

drugs1gene= pickle.load(open("drugs1gene.pkl","rb"));
     
drugs2= pickle.load(open("drugs2.pkl","rb"));


output = open('drugs2.pkl', 'wb')
pickle.dump(drugs2, output)
output.close()
output = open('drugs1gene.pkl', 'wb')
pickle.dump(drugs1gene, output)
output.close()

output = open('ma00pp.pkl', 'wb')
pickle.dump(ma00pp, output)
output.close()










     
