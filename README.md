# Python-based blast database program

Functions of this program:
* Computes pairwise blast alignments for two species' proteomes and stores their alignments in a relational database.
* Allows you to retrieve high scoring blast alignments for two proteins (specified by their accessions) from a relational database through python.
* Finds pairs of orthologous proteins that are mutually best blast hits in the species' proteomes.

This project was completed for the Georgetown graduate bioinformatics computing course in Fall 2015.

## Background
Orthologs are genes in different species that have evolved from a common ancestral gene due to speciation. Orthologous genes are transcribed, and then translated subsequently to orthologous proteins. These orthologous proteins retain the same functionality over the course of evolution in their respective species. Protein sequences that are closely related in sequence, are defined to be orthologs for this project.

## Installation
This program uses the following software tools:
* Biopython package - This package will be used to parse through XML and Fasta files. The package can be downloaded with instructions for installation within the following [link](http://biopython.org/wiki/Download).
* SQLobject package - This package will be used to initialize a relational database from the results of our blast. The package can be downloaded with instructions for installation within the following [link](http://www.sqlobject.org/download.html).
* NCBI blast tool - This tool will be used to conduct blast searches and provide us with all of the alignment results to be loaded into the relational database. The package can be downloaded with instructions for installation within the following [link](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download).
* SQLite studio - This is the relational database manager that you will use to create your database from python scripts. This program can be downloaded [here](https://sqlitestudio.pl/index.rvt?act=download).


## Project workflow
- Run a local blast with a query proteome against a subject proteome. Conduct a reciprocal blast. Full species proteome or genome sequences can be obtained from NCBI's blast database [here](https://ftp.ncbi.nlm.nih.gov/blast/db/). For this project we used species proteomes in FASTA format.
- Parse blast results for top hit alignment pairs, and load into relational database as a table.
- Create tables and initialize a new database for both species' proteomes.
- Create program files to access the database and extract information from relevant rows, in order to answer project questions.

## Instructions for use
Each species' proteome needs to be initialized as a database for blast. Create a folder or directory to store your database FASTA files. Change directory into this folder and run:
```
makeblastdb - help
makeblastdb - in "name or full path of proteome in FASTA format" -dbtype prot
```
This sets the database to whichever FASTA sequence you designate in blast, and the query proteome will be run against it. Be sure to run this command on the other proteome as well.

After setting your database sequences, run a local blast using NCBI's blast tool with the following command:
```
python local_blast.py "path of one species' proteome" "path of other species' proteome"
```
This will generate our blast results in XML format.

Inititate your database with the following script:
```
python model_blast.py
```
This will instantiate your protein database, and alignment database.

Load your relational database tables with the protein sequences:
```
python Blast_fasta_parser.py "Path for one species fasta proteome file" "Path for other species fasta proteome file"
```
Run this command to parse the blast results and load alignments that are high scoring (low expected value and high score) into an alignment table on the relational database:
```
python Blast_results_XML_parser.py
```
Retrieve blast alignment results with the following command:
```
python blast_alignment.py "protein ID number query"
```
Run this command to retrieve an orthologous protein to your protein query z:
```
python blast_find_orthologs.py "protein ID number query"
```


## Future directions for this project
* Create a better front end for user query.
* Upgrade relational database usage from SQLite studio to MySQL.
* Upload program that allows you to run command line local blast through python.

## Contact information
If there are any questions about this project, feel free to contact me at wongak626@gmail.com


