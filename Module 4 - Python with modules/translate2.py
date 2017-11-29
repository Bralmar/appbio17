#!/usr/bin/env python2

import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

with open(sys.argv[1],'rU') as ih:
	my_protein=[]
	for record in list(SeqIO.parse(ih, "fasta")):
		sys.stdout.write('>')
		sys.stdout.write(str(record.id))
		sys.stdout.write('\n')			
		if len(record.seq)>2:
			sys.stdout.write(str(record.seq.translate()))
			sys.stdout.write('\n')	
		else:
			print 'Too short to translate'
