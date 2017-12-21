#!/usr/bin/env python2

#there are more than 50% indels,
#at least 50% of amino acids are unique, OK
#no amino acid appears more than twice.


# To DO:
# -Make Histogram
# -Use tempfiles
# -Make comments
# -Make it easier to run (argparse?) 

import sys
from Bio import SeqIO
from Bio.Seq import Seq
import pdb
import os
import glob
from subprocess import check_output
import dendropy
from dendropy.calculate import treecompare
import tempfile






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
					break #Stopps looking in column if more than 2 characters are found
			count = {}

	return ShortList


def Printright(shortlist, Namelist, Columns):
	seqlist=[]
	donelist=[]
	finlist=[]
	Non_CleanList =[]
	Non_CleanList_Done =[]
	for m in range(len(Namelist)):		
		for i in range(len(shortlist)):
			seqlist.append(shortlist[i][m]) #Clean List
			Non_CleanList.append(Columns[i][m])	#Non Clean list
		donelist.append("".join(seqlist))
		Non_CleanList_Done.append("".join(Non_CleanList))
		Non_CleanList = []
		seqlist=[]
		finlist.append(donelist[m].replace(" ", ""))
		
	return finlist, Non_CleanList_Done



def tred(counter, Namelist, finlist, Non_CleanList_Done):
	with open('bajs', "w") as sh:
		for n in range(len(Namelist)):
			sh.write('\n' + '>' + Namelist[n] + '\n' + Non_CleanList_Done[n])
	with open('kiss', 'w') as ph: 			
		out=check_output(["fastprot", 'bajs'])
		ph.write(out)

	
	temp=tempfile.TemporaryFile(mode='w+t')			# Creates a temporary file "temp" and makes it readable as text. Writes output of fnj to it.
	temp.write(check_output(["fnj", "-O", "newick", "kiss"]))
	temp.seek(0)
	
	tns = dendropy.TaxonNamespace()
	t1 = dendropy.Tree.get(file=open('asymmetric_0.5.tree', 'r'), schema="newick", tree_offset=0, taxon_namespace=tns)
	t2 = dendropy.Tree.get(file=temp, schema="newick", tree_offset=0, taxon_namespace=tns)
	t1.encode_bipartitions()
	t2.encode_bipartitions()
	print(treecompare.symmetric_difference(t1, t2))
	temp.close()
	return



def main():
	longlist = []
	counter=0
	for filename in glob.glob(os.path.join(sys.argv[1], '*.msl')):
		counter+=1
		#Remove stuff
		Columns, Namelist = ReadFasta(filename)
		shortlist = CompareColumns(Columns)
		longlist.append(shortlist)
		finlist, Non_CleanList_Done =Printright(shortlist, Namelist, Columns)
		tred(counter, Namelist, finlist, Non_CleanList_Done)


		


if __name__=='__main__':
	main()


