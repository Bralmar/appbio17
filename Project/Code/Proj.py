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

path = sys.argv[1]
#path = 'data/test_folder'

def ReadFasta(filename):
	LetterList = []
	CompList = []
	VarList=[]
	Columns=[]
	Namelist=[]

	#Opens file and extracts each sequence as a list in a list
	with open(filename,'rU') as ih:
		for record in list(SeqIO.parse(ih, "fasta")):
			Namelist.append(record.id)
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
				
	return Columns, Namelist



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


def Printright(shortlist, Namelist, counter):
	seqlist=[]
	donelist=[]
	finlist=[]
	for m in range(len(Namelist)):		
		for i in range(len(shortlist)):
			seqlist.append(shortlist[i][m])
		donelist.append("".join(seqlist))
		seqlist=[]
		finlist.append(donelist[m].replace(" ", ""))

#	for n in range(len(Namelist)):
#		sys.stdout.write('\n' + '>' + Namelist[n] + '\n' + finlist[n])

	return finlist



def main():
	longlist = []
	counter=0
	for filename in glob.glob(os.path.join(path, '*.msl')):
		counter+=1
		Columns, Namelist = ReadFasta(filename)
		shortlist = CompareColumns(Columns)
		longlist.append(shortlist)
		finlist=Printright(shortlist, Namelist, counter)
		with open(str(counter), "w") as sh:
			for n in range(len(Namelist)):
				sh.write('\n' + '>' + Namelist[n] + '\n' + finlist[n])			





if __name__=='__main__':
	main()
