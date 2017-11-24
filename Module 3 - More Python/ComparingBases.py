#! /usr/bin/env python2
# How to run: ./ComparingBases.py simple1.fasta simple2.fasta
import sys
import math


def extract_sequence(x):
	'''Reads the fasta-format file and spearates the sequence from the name'''
	sequence=""
	name=""
	for line in x:	#extracts sequence and name of organism
		if line.startswith('>'):
			fullname=line.replace('\n','')
			
			if len(fullname)>10:	#restricts the name length to 10 characters
				name += fullname[0:10]
		else:
			sequence+=line
	for n in sequence:			#Error if sequence contains lower case letters.
		if n=='c' or n=='t' or n=='a' or n=='g':
			sys.stderr.write('Error. Sequence contains lower case letters.')
			sys.stdout.write('\n')
			sys.exit()
	return sequence, name




def compvec(sequence):
	''' Counts the number of bases in each string and returns list of base contetnts of each sequence.'''
	
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
	'''Takes a list of base contents of each sequence. Compares the distance between each sequence. '''
	diff = []
	diffList = []
	SqrtList = []
	totSqrtList=[]
	sqrt = []
	SqrtList2 = []
	for i in cocklist:
		
		for n in cocklist:
			
			for m in range(0,4):
				diff = math.pow((i[m]-n[m]),2)	#Calculates differences of each base, and squares the result. 
				diffList.append(diff)
				diff = []
			SqrtVal=(math.sqrt(sum(diffList)*0.25))	#Summs up each differences and divides it with 4.
			SqrtVal=round(SqrtVal, 4)
			SqrtList.append(str(SqrtVal))
			
			diffList = []
			SqrtVal = []
		
		SqrtList2.append(SqrtList)
		SqrtList = []
	
	return SqrtList2




def main():
	'''Main function which reads the input files, and calls the other functions. It also prints the output.'''
	cocklist = []
	totname = []
	for file in sys.argv[1:]:
		x = open(file, 'r')
		#Functions that do all calculations
		sequence, name=extract_sequence(x)
		totList = compvec(sequence)
		cocklist.append(totList)
		totname.append(name)
	
	totSqrtList = distance(cocklist)
	
	x = 0

	for line in totSqrtList:	#inserts name into the first position of each element in the list.
		
		line.insert(0, totname[x])
		x += +1
	
	sys.stdout.write(str(len(sys.argv[1:])))
	sys.stdout.write('\n')	
	sys.stdout.write('\n'.join([' '.join(['{:7}'.format(item) for item in row])  for row in totSqrtList]))#Prints the list in the phylip format. 

	sys.stdout.write('\n')
	return 

main()









