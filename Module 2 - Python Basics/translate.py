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
	finalseqs=[]
	for line in file:					#If line starts with >, it is saved into 'name' list. If not, it is saved into 'sequence' list, as one line per element.
		if line.startswith('>'):
			name.append(line.split())
			joined.append(''.join(sequence))
			sequence=[]
		else:
			sequence.append(line)
	joined.append(''.join(sequence))
	for unit in joined:				#replaces line-breakers with ''
		joinedsequence.append(unit.replace('\n',''))
	joinedsequence=list(filter(None, joinedsequence))

	return joinedsequence, name

wholeseq, name=extract_sequence()


def find_ORF(wholeseq):
	'''reads each reading frame, searching for stop codons. If present, the sequence from the last stop codon until the next is saved as an ORF'''
	orf=[]
	orfs=[]
	allorfs=[]
	alllongorf = []
	for k in wholeseq:
		for n in range(0,3): 						#reading frames, should start reading from first, second and third nucleotide.
			for i in range(n, len(k),3):		#reads from nucleotide no n to the last nucleotide, in jumps of three
				codon = k[i:i+3] 			#codon defined as nucleotide i to i+3
				orf.append(codon)					#ads all codons into one orf
				if codon == "TAA" or codon == "TGA" or codon == "TAG":	#if a codon is stop, the orf is saved as all codons until the stop.
					orfs=''.join(orf)				#Joins the comma spaced codons in the orf to one fluent string
					allorfs.append(orfs)			#Adds the found string into a list
					orf=[]							#Clear orf
			longorf=max(allorfs, key=len)
			allorfs =[]
		alllongorf.append(longorf)
	return alllongorf
orfs=find_ORF(wholeseq)


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
