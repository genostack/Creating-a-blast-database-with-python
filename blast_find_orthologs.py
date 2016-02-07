import sys
from model_blast import *
init()

idd = int(sys.argv[1])

def findortholog(idd):
    t = Protein.byProtid(idd)
    a =''
    for n in t.alignments:
        a = n.subject_ID
    t = Protein.byProtid(a)
    b = ''
    for n in t.alignments:
        b = n.subject_ID
    if b==idd:
        print idd,"is an ortholog of",a
    else:
        print "not orthog"
    
findortholog(idd)
