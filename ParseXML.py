import sys

from bs4 import BeautifulSoup


soup = BeautifulSoup(open(sys.argv[1]+'.xml'))



#print soup.findAll('block', attrs='full_text')


ftext = soup.findAll('block', attrs='full_text')
ft = unicode.join(u'\n', map(unicode,ftext))
FT = BeautifulSoup(ft)
#print FT.name


file = open(sys.argv[1]+'.txt', 'w') 
file.write('<DOC>\n<DOCNO>'+sys.argv[1]+'</DOCNO>\n<TEXT>\n')
file.write((FT.getText()).encode(('utf8')+'\n'))
file.write('</TEXT>\n</DOC>\n')
file.close() 
#print FT.block
#for string in FT.block.stripped_strings:
#    print(string)

#for child in FT.block.p.children:
#    print (child)








#print ft.string







#for line in ft:
#   print line.str
