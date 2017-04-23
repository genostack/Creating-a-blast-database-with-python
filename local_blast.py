# Special modules for running blast
from Bio.Blast.Applications import NcbiblastpCommandline
import sys

# Input two species' proteomes

if len(sys.argv) < 3:
	print >>sys.stderr, "Please provide paths for two proteome FASTA files"
	sys.exit(1)
	
blast_query_1 = str(sys.argv[1])
blast_query_2 = str(sys.argv[2])


blast_prog = 'blastp'

cmdline = NcbiblastpCommandline(cmd=blast_prog,
								query=blast_query_1,
								db=blast_query_2,
								outfmt=5,
								out="results.xml")
								
stdout, stderr = cmdline()

# Reciprocal Blast

cmdlineRecip = NcbiblastpCommandline(cmd=blast_prog,
								query=blast_query_2,
								db=blast_query_1,
								outfmt=5,
								out="results2.xml")
								
stdout, stderr = cmdlineRecip()