#! /usr/bin/env python2
import sys
import math

def extract_sequence(x):
	'''Reads the fasta-format file and spearates the sequence from the name'''
	sequence=""
	name=""
	for line in x:
		if line.startswith('>'):
			name=line.replace('\n','')
			
		else:
			sequence+=line
			
	return sequence, name




def compvec(sequence):
	
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

	



def main():
	cocklist = []
	for file in sys.argv[1:]:
		x = open(file, 'r')
		sequence, name=extract_sequence(x)
		templist = compvec(sequence)
		cocklist += templist

	return cocklist 

cocklist = main()




def distance(cocklist): 
	diff = []
	diffList = []
	sqrtList = []
	sqrt = []
	for n in range(0,4):
		diff = math.pow((cocklist[n]-cocklist[n+4]),2)
		diffList.append(diff)
		diff = []
	RovList = math.sqrt(sum(diffList)*0.25)
	print(RovList)
	return diffList

diffList = distance(cocklist)





