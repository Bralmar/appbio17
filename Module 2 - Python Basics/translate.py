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
	finalsequence =[]
	joinedsequence_upper=""
	joinedsequence=[]
	finalsequence=[]
	joinedsequence_upper=""
	for line in file:					#If line starts with >, it is saved into 'name' list. If not, it is saved into 'sequence' list, as one line per element.
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
		finalsequence.append(joinedsequence_upper)

	finalsequence=list(filter(None, finalsequence))

	return finalsequence, name

wholeseq, name=extract_sequence()
#print(sequence)
#print(wholeseq)
#print(name)

def find_ORF(wholeseq):
	'''reads each reading frame, searching for stop codons. If present, the sequence from the last stop codon until the next is saved as an ORF'''
	orf=[]
	orfs=[]
	allorfs=[]
	longorf=[]
	alllongorf=[]
	for k in wholeseq:
		if k[0] in 'ATCG' and len(k)>2:
			for n in range(0,3): 											#reading frames, should start reading from first, second and third nucleotide.
				for i in range(n, len(k),3):								#reads from nucleotide no n to the last nucleotide, in jumps of three
					codon = k[i:i+3] 										#codon defined as nucleotide i to i+3
					orf.append(codon)										#ads all codons into one orf
					if codon == "TAA" or codon == "TGA" or codon == "TAG" or len(codon)!=3:	#if a codon is stop, the orf is saved as all codons until the stop
						allorfs.append(''.join(orf))						#Adds the found string into a list
						orf=[]												#Clear orf
					elif n==len(k):
						allorfs.append(''.join(orf))
						orf=[]
			orf=[]
			longorf=max(allorfs, key=len)
			allorfs=[]
			alllongorf.append(longorf)
		else:
			alllongorf.append(k)
	return alllongorf
longorf=find_ORF(wholeseq)


def translate(longorf):
	'''translates the longest ORF into a polypeptide'''
	pept = ""
	peptlist=[]
	dictionary={
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TGC':'C', 'TGT':'C',
	'TGG':'W', 'TAA':'', 'TAG':'', 'TGA':'',
	}
	for k in longorf:
		if len(k)>2:
			for i in range(0, len(k),3):	#reads from nucleotide no n to the last nucleotide, in jumps of three
				if k[i:i+3] in dictionary:
					pept += dictionary[k[i:i+3]]
				elif len(k[i:i+3])>2:
					pept += 'X'
			peptlist.append(pept)
			pept=""
		else:
			peptlist.append('')
	return peptlist #codon_list
peptlist=translate(longorf)

for n in range(0, len(peptlist)):
	print(name[n])
	print(peptlist[n]+'\n')

def translate(orfs):
	'''translates the longest ORF into a polypeptide'''
	pept = ("")
	peptlist=[]
	dictionary={
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TGC':'C', 'TGT':'C',
	'TGG':'W', 'TAA':'', 'TAG':'', 'TGA':'',
	}
	for k in orfs:
		if len(k)>2:
			for i in range(0, len(k),3):		#reads from nucleotide no n to the last nucleotide, in jumps of three
				if k[i:i+3]  in dictionary:		#codon defined as nucleotide i to i+3
					pept += dictionary[k[i:i+3]]
				elif len(k[i:i+3])>2:
					pept+="X"
			peptlist.append(pept)
			pept =""
		else:
			peptlist.append("X")


	return peptlist #codon_list

peptlist = translate(orfs)

for n in range(0, len(peptlist),1):
    print(name[n])
    print(peptlist[n]+'\n')
