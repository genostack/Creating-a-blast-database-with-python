from sqlobject import *
import os.path, sys

dbfile = 'blast.db3'

def init(new=False):
    # Magic formatting for database URI
    conn_str = os.path.abspath(dbfile)
    conn_str = 'sqlite:'+ conn_str
    # Connect to database
    sqlhub.processConnection = connectionForURI(conn_str)
    if new:
        # Create new tables (remove old ones if they exist)
        Protein.dropTable(ifExists=True)
        Alignment.dropTable(ifExists=True)
        Protein.createTable()
        Alignment.createTable()

class Protein(SQLObject):
    protid = IntCol(alternateID=True)
    protein_name = StringCol()
    organism_name = StringCol()
    alignments = MultipleJoin("Alignment")

class Alignment(SQLObject):
    subject_ID = IntCol()
    protein = ForeignKey("Protein")
    E_value = FloatCol()
    score = FloatCol()
    query_sequence = StringCol()
    match_sequence = StringCol()
    subject_sequence = StringCol()
    
    


