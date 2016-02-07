import Bio.SeqIO
import sys
from model_blast import *

init(new=True)

# Check the input
if len(sys.argv) < 2:
    print >>sys.stderr, "Please provide a sequence file"
    sys.exit(1)

# Get the sequence filename
seqfilename1 = sys.argv[1]
seqfilename2 = sys.argv[2]

for i in seqfilename1, seqfilename2:
    
    # Open the FASTA file and iterate through its sequences
    seqfile = open(i)
    for seq_record in Bio.SeqIO.parse(seqfile, "fasta"):
        # Print out the various elements of the SeqRecord
        l = seq_record.id
        y = l.split('|')
        accession = int(y[1])
        a = seq_record.description
        b = a.split('|')
        d = b[4].split('[')
        protein_name = d[0]
        c = a.split('[')
        p_name = c[1].strip('[')
        organism_name = p_name.strip(']')
    

        p = Protein(protid = accession, protein_name = protein_name,
                 organism_name = organism_name)
                 

    
   
    seqfile.close()
