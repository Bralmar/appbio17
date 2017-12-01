#!/usr/bin/env python
# chmod +x blast_parsing.py insert in terminal before script

from math import exp
import Bio.Blast
import sys
from Bio.Blast import NCBIXML
from Bio.Blast.NCBIXML import parse
import re

#######################################################
def evalue_threshold():
	'''Removes all alignments with E-value below the threshold'''
	e_value=exp(1e-60)

	b = sys.argv[2]
	c = sys.argv[1]
	
	accessions = []

	xml_file = open(b)
	blast_out = NCBIXML.parse(xml_file)
	for record in blast_out:
		for alignment in record.alignments:
			if re.search(c, str(alignment)):				# Searching for command line argument that matches "Hit_id", "Hit_def", or "Hit_accession"
				for hsp in alignment.hsps:
					if hsp.expect < e_value:			# Saves only alignments with E-value below threshold
						accessions.append(alignment.accession)
	if len(accessions) == 0:
		sys.stderr.write('Warning: No hits')
		sys.stderr.write('\n')
		exit()

	return accessions

#######################################################
def sort_duplicates(accessions):
	'''Extracts all duplicates'''
	seen = set()
	duplicates = set()

	for line in accessions:	
		if line not in seen:
			seen.add(line)							# Contains one copy of all accession numbers for the alignments
		else:
			duplicates.add(line)						# Contains the duplicates

	return seen, duplicates

#######################################################
def print_nonduplicates(seen, duplicates):
	'''Prints query accession, target accession, score, and E-value for the one of all duplicates with the lowest E-value'''
	for line in seen:
		if line not in duplicates:
			b = sys.argv[2]
			c = sys.argv[1]	
			xml_file3 = open(b)
			blast_out3 = NCBIXML.parse(xml_file3)
			for record in blast_out3:
				for alignment in record.alignments:
					if re.search(line, str(alignment)):				# Finds the alignment with correspoding accession number
						for hsp in alignment.hsps:
							sys.stdout.write(str(record.query))		
							sys.stdout.write('\t')
							sys.stdout.write(str(alignment.accession))
							sys.stdout.write('\t')
							sys.stdout.write(str(hsp.expect))
							sys.stdout.write('\t')
							sys.stdout.write(str(hsp.score))
							sys.stdout.write('\n')

#######################################################
def print_duplicates(seen, duplicates):
	'''Prints query accession, target accession, score, and E-value for every alignment without a duplicate'''
	b = sys.argv[2]
	c = sys.argv[1]
	e_value=exp(1e-60)

	xml_file2 = open(b)
	blast_out2 = NCBIXML.parse(xml_file2)
	for line in duplicates:
		a = line
		for record in blast_out2:
			for alignment in record.alignments:
				if re.search(a, str(alignment)):
					for hsp in alignment.hsps:
						if hsp.expect < e_value:				# Finds all alignment duplicates and selects the one with the lowest E-value
							e_value = hsp.expect
		sys.stdout.write(str(record.query))
		sys.stdout.write('\t')
		sys.stdout.write(str(alignment.accession))
		sys.stdout.write('\t')
		sys.stdout.write(str(hsp.expect))
		sys.stdout.write('\t')
		sys.stdout.write(str(hsp.score))
		sys.stdout.write('\n')

#######################################################
def main():										
	accessions = evalue_threshold()
	seen, duplicates = sort_duplicates(accessions)
	print_nonduplicates(seen, duplicates)
	print_duplicates(seen, duplicates)		

if __name__ == "__main__":							
	main()




