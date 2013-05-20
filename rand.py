import sys
import re
import os
os.chdir('D:')
f=open("7","r")
w=[]
subl=[]
subd={}
fr=f.read()
match=re.search('subject:(.+)\n',fr.lower())
if match:
    print ('found',match.group(1))
    subl=subl+[w for w in re.split('\W',match.group(1)) if w]
    print (subl)
    for element in subl:
        if element in subd:
            subd[element]+=1
        else: subd[element]=1
    print (subd.items())
match=re.search("filename:.+\n([.+^"----"])",fr.lower())
print (match.group())
f.close()
