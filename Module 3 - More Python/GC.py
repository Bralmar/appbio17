

def read_fasta()
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
			joinedsequence_upper=i.upper()
			finalsequence.append(joinedsequence_upper)
		finalsequence=list(filter(None, finalsequence))	#removes the first empty unit in the list joinedsequence
		return finalsequence, name
