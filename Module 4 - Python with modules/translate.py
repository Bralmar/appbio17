#!/usr/bin/env python2

import sys
from Bio import SeqIO
from Bio.Seq import Seq
#from Bio.Alphabet import IUPA

def extract_seq(file):
	with open(sys.argv[1],'r') as file:
		name=[]
		joined=[]
		sequence=[]
		joinedsequence=[]
		wholeseq=[]
		sequences=[]
		joinsequence_upper=[]
		for line in file:
			if line.startswith('>'):
				name.append(line.replace('\n',''))
				joined.append(''.join(sequence))
				sequence=[]
			else:
				sequence.append(line)
		joined.append(''.join(sequence))
		for unit in joined:				#replaces line-breakers with ''
			joinedsequence.append(unit.replace('\n',''))
		for i in joinedsequence: 	
			joinedsequence_upper = i.upper()
			sequences.append(joinedsequence_upper)
		sequences=list(filter(None, sequences))

		return sequences, name

sequences, name= extract_seq(file)

def translation(sequences):
	proteinseqs=""
	seq=[]
	aa_seq=[]
	for row in sequences:
		if len(row)>2:
			seq=Seq(row)
			aa_seq=seq.translate()
			proteinseqs += aa_seq + '\n'
			#print aa_seq
		else:
			print 'hej' 
	return proteinseqs

proteinseqs=translation(sequences)
print proteinseqs
	
	
