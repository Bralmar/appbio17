

def extract_sequence():
	'''Reads the fasta-format file and spearates the sequence from the name'''
	raw=input('Which file? ')
	file=open(raw, 'r')
	sequence=""
	name=""
	for line in file:					#If line starts with >, it is saved into 'name' list. If not, it is saved into 'sequence' list, as one line per element.
		if line.startswith('>'):
			name=line.replace('\n','')
		else:
			sequence+=line
	return sequence, name
sequence, name=extract_sequence()


def GC_count(sequence):
	gcount=sequence.count('G')
	ccount=sequence.count('C')
	gccount=gcount+ccount
	totcount=len(sequence)
	content=gccount/totcount
	return content
content=GC_count(sequence)


print(name)
print(content)

