# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:44:17 2017

@author: Emil
"""

def extract_sequence():
	raw=input('Which file? ')
	file=open(raw, 'r')
	sequence=[]
	name=[]
	joined=[]
	joinedsequence=[]
	wholeseq=[]
	for line in file:					#If line starts with >, it is saved into 'name' list. If not, it is saved into 'sequence' list, as one line per element.
		if line.startswith('>'):
			name.append(line.split())
			#joined.append(sequence)
		else:
			sequence.append(line)
	for line in sequence:				#replaces line-breakers with ''
		joinedsequence.append(line.replace('\n',''))
	wholeseq=''.join(joinedsequence)	#joins each element into one
	#print(joined)
	return wholeseq, name
wholeseq, name=extract_sequence()


def find_ORF(wholeseq):
	orf=[]
	orfs=[]
	allorfs=[]
	for n in range(0,2): 				#reading frames, should start reading from first, second and third nucleotide.
		for i in range(n, len(wholeseq),3):	#reads from nucleotide no n to the last nucleotide, in jumps of three
			codon = wholeseq[i:i+3] 	#codon defined as nucleotide i to i+3
			orf.append(codon)			#ads all codons into one orf
			if codon == "TAA" or codon == "TGA" or codon == "TAG":	#if a codon is stop, the orf is saved as all codons until the stop.
				orfs=''.join(orf)
				allorfs.append(orfs)
				orf=[]
	return allorfs
orfs=find_ORF(wholeseq)
#print(orfs)
#print(len(orfs))
