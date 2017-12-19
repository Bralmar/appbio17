#!/usr/bin/env python2

#there are more than 50% indels,
#at least 50% of amino acids are unique, OK
#no amino acid appears more than twice.

import sys
from Bio import SeqIO
from Bio.Seq import Seq
import pdb
import os
import glob

#path = 'data/asymmetric_0.5'
path = 'data/test_folder'

def ReadFasta(filename):
	LetterList = []
	CompList = []
	VarList=[]
	Columns=[]

	#Opens file and extracts each sequence as a list in a list
	with open(filename,'rU') as ih:
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



def CompareColumns(Columns):
	RemList = []
	ShortList = []
	count = {}
	New_ShortList = []
	

	for i in range(len(Columns)):
		RemList.append(''.join(set(Columns[i])))

	
	for m in range(len(RemList)):
		if float(len(RemList[m])) / len(Columns[m]) >= 0.5 or Columns[m].count('-')/float(len(Columns[m])) >= 0.5:
			ShortList.append(Columns[m].replace(Columns[m],len(Columns[m])*' '))
		else:			
			for s in Columns[m]:
				if count.has_key(s):
					count[s] += 1
				else:
					count[s] = 1
			for key in count:
				if count[key] > 2:
					ShortList.append(Columns[m])
			count = {}

	return ShortList



def main():
	longlist = []
	for filename in glob.glob(os.path.join(path, '*.msl')):
		Columns = ReadFasta(filename)
		shortlist = CompareColumns(Columns)
		longlist.append(shortlist)
	sys.stdout.write(str(longlist) + '\n')
	


if __name__=='__main__':
	main()




