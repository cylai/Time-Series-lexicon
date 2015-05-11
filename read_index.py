#!/usr/bin/env python
import sys
from optparse import OptionParser

if len(sys.argv) < 1:
    print 'Please use -h to see how to use this program.'
    sys.exit()

usage = "read_index [options] -p path"

parser = OptionParser(usage = usage)

parser.add_option("-p", "--path", dest="path",
        help="path for index", type="string", default="1996")

(options, args) = parser.parse_args()

words=[]
fileinput = open("./index_lemur/"+options.path+"/index.txt")

line = fileinput.readline() # remove the first line
line = fileinput.readline()
winfo = line.rstrip().rsplit(" ")
while 1:
    if not line: break

    word=[]
    docs=[]
    value=[]
    while 1:
        line = fileinput.readline()
        if line.startswith("\t"): 
            line = line.lstrip().rsplit(" ")
            line = [int(x) for x in line]
            docs.append(line[0:2])
        else:
            break

    docs = dict(docs)

    value.append(int(winfo[1])) # collect word frequency
    value.append(int(winfo[2])) # document frequency
    value.append(docs)

    word.append(winfo[0]) # key: word
    word.append(value) # value: col_word_freq, doc_freq, docs_hash

    winfo = line.rstrip().rsplit(" ")

    words.append(word)

words = dict(words)

output = open("./index_lemur/"+options.path+"/index.pkl", 'wb')
#import pickle
import cPickle as pickle
pickle.dump(words, output, 2)
output.close()

###################################################
