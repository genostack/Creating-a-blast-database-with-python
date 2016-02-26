# Creating-a-blast-database-with-python
- Computes pairwise blast alignments for any two species' proteomes and stores the alignments in SQL relational database.
- Allows you to retrieve two proteins specified by their accessions from the relational database. 
- Allows you to retrieve pairs of orthologous proteins that are mutually best hits in the species' proteomes.
- Provides the blast alignment for a protein query specified by the genbank accession number in blast_alignment.py file .
- Also provides the bit score and e-value of the alignment. Derived organism and protein name of the query is also outputted as a result.
- Provides the orthologous protein accession number, when a protein is queried with blast_find_orthologs.py file.

Testing the program:
- Protein accession GI#: 78706572, or waclaw protein, was run with the program file blast_alignment.py to test the alignment retrieval program.
- The same protein was used to test the blast_find_orthologs.py program file

Project workflow:
- Run a local blast with a query proteome against a subject proteome. Conduct a reciprocal blast.
- Parse blast results for top hit alignment pairs, and extract relevant information to be loaded into tables.
- Create tables and initialize a new database for your blast results.
- Create program files to access the database and extract information from relevant rows, in order to answer project questions.

Instructions for installation:
- Install Sqlite to your computer from: https://www.sqlite.org/download.html
- Download all of the files
- Make sure to have drosoph-ribosome.fasta and yeast-ribosome.fasta in your designated home folder
- Conduct local blasts.
- Run blast_FASTA_parser.py.
- Run Blast_results_XML_parser.py.
- Run blast_alignment.py to find alignment with query protein (genbank accession input).
- Run blast_find_ortohologs.py to find orthologous protein pairs with query protein (genbank accession input).


