from Bio.Blast import NCBIXML
from model_blast import *

init()

result_handle2 = open("results2.xml")
for blast_result in NCBIXML.parse(result_handle2):
    for alignment in blast_result.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 1e-100 and hsp.score > 1000.0:
                l = alignment.title
                y = l.split('|')
                subject_ID1 = y[3]
                a = blast_result.query
                b = a.split('|')
                n = Protein.byProtid(int(b[1]))
                e_value = hsp.expect
                bit_score = hsp.score
                query_sequence1 = hsp.query
                match_sequence1 = hsp.match
                subject_sequence1 = hsp.sbjct
                
               
                t = Alignment(subject_ID = int(subject_ID1),
                              protein = n,
                              E_value = e_value,
                              score = bit_score,
                              query_sequence = query_sequence1,
                              match_sequence = match_sequence1,
                              subject_sequence = subject_sequence1)

result_handle = open("results.xml")
for blast_result in NCBIXML.parse(result_handle):
    for alignment in blast_result.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 1e-100 and hsp.score > 1000.0:
                l = alignment.title
                y = l.split('|')
                subject_ID1 = y[3]
                a = blast_result.query
                b = a.split('|')
                n = Protein.byProtid(int(b[1]))
                e_value = hsp.expect
                bit_score = hsp.score
                query_sequence1 = hsp.query
                match_sequence1 = hsp.match
                subject_sequence1 = hsp.sbjct
                
               
                t = Alignment(subject_ID = int(subject_ID1),
                              protein = n,
                              E_value = e_value,
                              score = bit_score,
                              query_sequence = query_sequence1,
                              match_sequence = match_sequence1,
                              subject_sequence = subject_sequence1)