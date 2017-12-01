#!/usr/bin/env python2
from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Blast import NCBIXML
import sys    

def Blastdatbitch():
	with open(sys.argv[1], 'rU') as pedo:
		for record in list(SeqIO.parse(pedo, "fasta")):
			phile = NCBIWWW.qblast("blastp", "nr", record.seq)
			sadasd = NCBIXML.parse(phile)
			sys.stdout.write(sadasd)			
	return
Blastdatbitch()


