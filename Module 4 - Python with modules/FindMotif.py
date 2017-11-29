#!/usr/bin/env python2

import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import motifs
import re 


def FindMotif():
	counter = 0
	pattern = re.compile(".*KL[EI]{2,}K.*")
	with open(sys.argv[1],'rU') as ih:
		for record in list(SeqIO.parse(ih, "fasta")):
			m = pattern.match(str(record.seq))
			if m:
				sys.stdout.write('>')
				sys.stdout.write(str(record.id))
				sys.stdout.write('\n') 
				sys.stdout.write(str(record.seq))
				sys.stdout.write('\n') 
				counter += 1
	print(counter)
	return



FindMotif()
