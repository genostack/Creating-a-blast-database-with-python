import sys
from model_blast import *
init()


try:
    protid = int(sys.argv[1])
except IndexError:
    print >>sys.stderr, "Need a Protien accession id argument"
    sys.exit(1)
except ValueError:
    print >>sys.stderr, "Protein accession id should be an integer"
    sys.exit(1)
    

try:
    t = Protein.byProtid(protid)
except SQLObjectNotFound:
    print >>sys.stderr, "Protein:",protid,"does not exist"
    sys.exit(1)

for n in t.alignments:
    print n.query_sequence[0:75]
    print n.match_sequence[0:75]
    print n.subject_sequence[0:75]
    print "Subject protein:", n.subject_ID
    print "Query protein:",t.protid,
    print "Query protein name:",t.protein_name
    print "Query protein organism:",t.organism_name
    print "E-value:",n.E_value
    print "Bit score:",n.score
