#!/usr/bin/env python2

import sys
import tempfile
from subprocess import Popen, PIPE
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

def read_fasta():
	with open(sys.argv[1],'rU') as ih:
		for record in list(SeqIO.parse(ih, "fasta")):
			fp = tempfile.TemporaryFile() 
			if len(record.id) > 9:
				fp.write(str(record.id[0:9]) + '\n' + str(record.seq) + '\n')
	
			elif len(record.id) < 9:				
				fp.write(str(record.id).ljust(10) + '\n' + str(record.seq) + '\n')

	process = Popen(['phylip neighbor', fp], stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()
	

read_fasta()


