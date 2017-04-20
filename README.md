# Python-based blast database program

Functions of this program:
* Computes pairwise blast alignments for two species' proteomes and stores their alignments in a relational database.
* Allows you to retrieve the blast alignment for two proteins (specified by their accessions) from the relational database.
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
- Run a local blast with a query proteome against a subject proteome. Conduct a reciprocal blast.
- Parse blast results for top hit alignment pairs, and load into relational database as a table.
- Create tables and initialize a new database for both species' proteomes.
- Create program files to access the database and extract information from relevant rows, in order to answer project questions.

## Future directions for this project
* Create a better front end for user query
* Upgrade relational database usage from SQLite studio to MySQL

## Contact information
If there are any questions about this project, feel free to contact me at wongak626@gmail.com


