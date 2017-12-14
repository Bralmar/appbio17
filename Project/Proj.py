#!/usr/bin/env python2

import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import motifs
import re 


def ReadFasta():
	LetterList = []
	CompList = []
	with open(sys.argv[1],'rU') as ih:
		for record in list(SeqIO.parse(ih, "fasta")):
			#sys.stdout.write('>'+ str(record.id) + '\n'
			for i in range(0, len(record.seq)):
				LetterList.append(record.seq[i])
				
					
					

				CompList.append(LetterList)
				
				#''.join(CompList)
			LetterList = ""

	#print(LetterList)
	#print(CompList)		
	return


ReadFasta()
