#!/usr/bin/env python
import sys
import math
import mlpy
import numpy as np
import cPickle as pickle
from pymur import *
from scipy.stats.stats import pearsonr
from operator import itemgetter, attrgetter
i = Index("../DATA/News_index/"+sys.argv[2])

SPindex = []
#open stockprice file
SPfile = open("../DATA/stockprice/"+sys.argv[1]+"/"+sys.argv[1]+sys.argv[2]+'.txt')
for l in SPfile:
    SPindex.append(l.strip())
SPlist = []
for y in SPindex:
    SPlist.append(float(y))
if sys.argv[2] == '2000':
    Uterm = 212714
if sys.argv[2] == '2001':
    Uterm = 202619
if sys.argv[2] == '2002':
    Uterm = 211797
if sys.argv[2] == '2003':
    Uterm = 209751
if sys.argv[2] == '2004':
    Uterm = 200128
if sys.argv[2] == '2005':
    Uterm = 204268
if sys.argv[2] == '2006':
    Uterm = 209339
if int(sys.argv[2]) % 4 ==0:
    YEAR = 366
else:
    YEAR = 365
#print len(doc)
pkl_file = open('../DATA/News_index/'+sys.argv[2]+'.pkl', 'rb')
words = pickle.load(pkl_file)
pkl_file.close()
#print len(doc2)
writeCor = open("./DCor/"+sys.argv[1]+"/"+sys.argv[1]+sys.argv[2]+"Cor.txt", 'wr') 
#f = open("Pcorrelation.txt", 'wr')
Cor =[]
Test = []

for term_id in range(1, Uterm+1):
    tfIndoc = []
    term = i.term(term_id)
    wordTF = []    
    for x in range(1, YEAR+1):
        try:
            wordTF.append(words[term][2][x])
        except:
            wordTF.append(0)    
    #f.write(term+" "+" ".join(map(lambda x: str(x), pearsonr(tmpD, SPnum))))
    #f.write("\n") 
    wordTFArray = np.array(wordTF)
    indexArray = np.array(SPlist)
    dist, cost, path = mlpy.dtw_std(wordTFArray, indexArray, dist_only=False)
    
    Cor.append([term, pearsonr(wordTFArray[path[0]], indexArray[path[1]])[0],pearsonr(wordTFArray[path[0]],indexArray[path[1]])[1]]) 

Test = sorted(Cor, key=lambda co : co[1], reverse=True)
#Test = sorted(Cor, key=lambda Co : Co[0])
#print len(Test)
for u in range(0, len(Test)):
    writeCor.write(str(Test[u])+"\n")
    #print Test[u]
    #if len(tmpD) != 366:
    #    ErNum +=1
    #    ErList.append(term)
writeCor.close()
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
