# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:44:17 2017

@author: Emil
"""

def extract_sequence():
	'''Reads the fasta-format file and spearates the sequence from the name'''
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
	print(joinedsequence)
	return wholeseq, name
wholeseq, name=extract_sequence()
<<<<<<< HEAD
print(wholeseq)
=======
#print(sequence)
#print(wholeseq)
print(name)
>>>>>>> 2052dace59b4505b6d76aebbc3632542c9451b33

def find_ORF(wholeseq):
	'''reads each reading frame, searching for stop codons. If present, the sequence from the last stop codon until the next is saved as an ORF'''
	orf=[]
	orfs=[]
	allorfs=[]
	for n in range(0,3): 						#reading frames, should start reading from first, second and third nucleotide.
		for i in range(n, len(wholeseq),3):		#reads from nucleotide no n to the last nucleotide, in jumps of three
			codon = wholeseq[i:i+3] 			#codon defined as nucleotide i to i+3
			orf.append(codon)					#ads all codons into one orf
			if codon == "TAA" or codon == "TGA" or codon == "TAG":	#if a codon is stop, the orf is saved as all codons until the stop.
				orfs=''.join(orf)				#Joins the comma spaced codons in the orf to one fluent string
				allorfs.append(orfs)			#Adds the found string into a list
				orf=[]							#Clear orf
	return allorfs
orfs=find_ORF(wholeseq)


def find_longest_orf(orfs):
	'''finds the longest orf in the collection'''
	longorf=max(orfs, key=len)
	return longorf

longorf=find_longest_orf(orfs)
#print(longorf)


#def translate(longorf):
#	'''translates the longest ORF into a polypeptide'''
#	pept = ("")
#	dictionary={
#    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
#    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
#    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
#    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
#    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
#    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
#    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
#    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
#    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
#    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
#    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
#    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
#    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
#    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
#    'TAC':'Y', 'TAT':'Y', 'TGC':'C', 'TGT':'C',
#	'TGG':'W', 'TAA':'_', 'TAG':'_', 'TGA':'_',
#	}
#	for i in range(0, len(longorf),3):		#reads from nucleotide no n to the last nucleotide, in jumps of three
#		codon = longorf[i:i+3] 			#codon defined as nucleotide i to i+3
#		pept += dictionary[codon]
#	print(pept)
#	return pept #codon_list
#translate(longorf)
