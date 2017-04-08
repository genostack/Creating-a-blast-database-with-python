# Python-based blast database program

Functions of this program:
* Computes pairwise blast alignments for two species' proteomes and stores their alignments in a relational database.
* Allows you to retrieve the blast alignment for two proteins (specified by their accessions) from the relational database.
* Finds pairs of orthologous proteins that are mutually best hits in the species' proteomes.

This project was completed for the Georgetown Graduate Bioinformatics Computing course in Fall 2015.

# # Background
Orthologs are genes in different species that have evolved from a common ancestral gene due to speciation. Orthologous genes are transcribed, and then translated subsequently to orthologous proteins. These orthologous proteins retain the same functionality over the course of evolution in their respective species. 

# # Installation
This program uses the following software tools:


Testing the program:
- Protein accession GI#: 78706572, or waclaw protein, was run with the program file blast_alignment.py to test the alignment retrieval program.
- The same protein was used to test the blast_find_orthologs.py program file

Project workflow:
- Run a local blast with a query proteome against a subject proteome. Conduct a reciprocal blast.
- Parse blast results for top hit alignment pairs, and extract relevant information to be loaded into tables.
- Create tables and initialize a new database for your blast results.
- Create program files to access the database and extract information from relevant rows, in order to answer project questions.

# # Future directions for this project
* Run this project on 
# # Contact information
If there are any questions about this project, feel free to contact me at wongak626@gmail.com


