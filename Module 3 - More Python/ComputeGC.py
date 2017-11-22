#! /usr/bin/env python2
import sys

def extract_sequence(x):
	'''Reads the fasta-format file and spearates the sequence from the name'''
	sequence=""
	name=""
	for line in x:
		if line.startswith('>'):
			name=line.replace('\n','')
			#print(name)
		else:
			sequence+=line
			#print(sequence)
	return sequence, name




def GC_count(sequence):
	gcount=sequence.count('G')
	ccount=sequence.count('C')
	acount=sequence.count('A')
	tcount=sequence.count('T')
	gccount=gcount+ccount
	totcount=gcount+ccount+acount+tcount
	content=float(gccount)/totcount
	return content, totcount




def main():
	for file in sys.argv[1:]:
		x = open(file, 'r')
		sequence, name=extract_sequence(x)
		content, totcount=GC_count(sequence)
		print(name)
		print(totcount)
		print(content)
	return

#sequence, name=extract_sequence(x)
#content=GC_count(sequence)
main()



#print(name)
#print(content)

