#!/usr/bin/env python

#there are more than 50% indels,
#at least 50% of amino acids are unique, OK
#no amino acid appears more than twice.

import sys
from Bio import SeqIO
from Bio.Seq import Seq
import pdb
import os


def ReadFasta():
	LetterList = []
	CompList = []
	VarList=[]
	Columns=[]

	#Opens file and extracts each sequence as a list in a list
	for f in os.listdir(sys.argv[1]):
		with open(f,'rU') as ih:
			for record in list(SeqIO.parse(ih, "fasta")):
				for i in range(0, len(record.seq)):
					LetterList.append(record.seq[i])
					
				CompList.append("".join(LetterList))
				LetterList = []	

		#Extracts each column for each sequence and saves in a list (Columns)
			for i in range(0, len(record.seq)):
				for m in range(len(CompList)):
					VarList.append(CompList[m][i])
				Columns.append("".join(VarList))
				VarList=[]
				
	return Columns

Columns = ReadFasta()

def CompareColumns(Columns):
	RemList = []
	ShortList = []

	for i in range(len(Columns)):
		RemList.append(''.join(set(Columns[i])))

	
	for m in range(len(RemList)):
		if float(len(RemList[m])) / len(Columns[m]) >= 0.5 or Columns[m].count('-')/float(len(Columns[m])) >= 0.5 :
			ShortList.append(Columns[m].replace(Columns[m],len(Columns[m])*' '))
		else:			
			ShortList.append(Columns[m])
	#print(len(ShortList))
	print(ShortList)

CompareColumns(Columns)
