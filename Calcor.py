#!/usr/bin/env python
import sys
import math
import cPickle as pickle
from pymur import *
from scipy.stats.stats import pearsonr
from operator import itemgetter, attrgetter
i = Index("index")

SPindex = []
SPfile = open("SPindex")
for l in SPfile:
    SPindex.append(l.strip())


SPnum = []
for y in SPindex:
    SPnum.append(float(y))
    
#print len(doc)
pkl_file = open('./index_lemur/2000/indexE.pkl', 'rb')
words = pickle.load(pkl_file)
pkl_file.close()
#print len(doc2)
fC = open("Test2", 'wr') 
#f = open("Pcorrelation.txt", 'wr')
Cor =[]
#ErNum = 0
#ErList =[]


Test = []

for term_id in range(1, 212715):
    tfIndoc = []
    term = i.term(term_id)

    tmpD = []    
    for x in range(1, 367):
         try:
             tmpD.append(words[term][2][x])
         except:
            tmpD.append(0)
    

    #f.write(term+" "+" ".join(map(lambda x: str(x), pearsonr(tmpD, SPnum))))
    #f.write("\n")    
    Cor.append([term, pearsonr(tmpD, SPnum)[0],pearsonr(tmpD,SPnum)[1]]) 



Test = sorted(Cor, key=lambda co : co[1], reverse=True)
#Test = sorted(Cor, key=lambda Co : Co[0])
#print len(Test)

for u in range(0, len(Test)):
    fC.write(str(Test[u])+"\n")
    #print Test[u]
    #if len(tmpD) != 366:
    #    ErNum +=1
    #    ErList.append(term)
fC.close()
        #print(tfIndoc)
#print ErNum
#print ErList
#print doc[3]
#print doc2[team]
#print doc
#print doc[3]

"""
#for doc_id in range(1, len(i)+1):
    doc = i.document(doc_id)
    docLen = len(doc)
    terms = dict(zip (set(doc), map (doc.count, set(doc))))
    features = []
    #features.append[terms[0]]    
#print(terms)
"""    


#print doc[0].count
