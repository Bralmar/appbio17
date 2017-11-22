#! /usr/bin/env python2
# How to run: ./ComparingBases.py simple1.fasta simple2.fasta
import sys
import math

def extract_sequence(x):
	'''Reads the fasta-format file and spearates the sequence from the name'''
	sequence=""
	name=""
	for line in x:
		if line.startswith('>'):
			fullname=line.replace('\n','')
			
			if len(fullname)>10:
				name += fullname[0:10]
		else:
			sequence+=line
	
	return sequence, name




def compvec(sequence):
	''' Counts the number of bases in each string'''
	
	gcount=sequence.count('G')
	ccount=sequence.count('C')
	acount=sequence.count('A')
	tcount=sequence.count('T')
	
	totcount=gcount+ccount+acount+tcount

	gcomp = gcount/float(totcount)
	ccomp = ccount/float(totcount)
	tcomp = tcount/float(totcount)
	acomp = acount/float(totcount)

	totList = [gcomp, ccomp, tcomp, acomp]

	return totList

	


def distance(cocklist): 
	diff = []
	diffList = []
	SqrtList = []
	totSqrtList=[]
	sqrt = []
	totSqrtList2 = []
	for i in cocklist:
		for n in cocklist:
			for m in range(0,4):
				diff = math.pow((i[m]-n[m]),2)
				diffList.append(diff)
				diff = []
			SqrtVal=(math.sqrt(sum(diffList)*0.25))
			SqrtList.append(SqrtVal)
			diffList = []
			SqrtVal = []
		#totSqrtList.append(SqrtList)
	print(SqrtList)

	return SqrtList




def main():
	cocklist = []
	totname = []
	for file in sys.argv[1:]:
		x = open(file, 'r')
		sequence, name=extract_sequence(x)

		totList = compvec(sequence)
		cocklist.append(totList)
		totname.append(name)
	
	totSqrtList = distance(cocklist)
		
	
	for n in range(0,len(sys.argv[1:])):
		for i in range(0, len(totSqrtList)):
			print(totname[n], totSqrtList[i:i+4])

	return cocklist 

main()









