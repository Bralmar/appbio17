#!/usr/bin/env python2

from Bio import SeqIO
from Bio.Blast import NCBIXML
#from Bio import SearchIO
import sys
import re

def cleaning():
	accessions=[]
	counter=0
	with open(sys.argv[1], 'rU') as fil:

    		indata=NCBIXML.parse(fil)

		for record in indata:		
			
			for alignment in record.alignments:
				
				if re.search(sys.argv[2], str(alignment)):
					
					for hsp in alignment.hsps:
						
						if hsp.expect<10**(-20):

							sys.stdout.write(str(record.query[0:20]))
							sys.stdout.write('\t')
							sys.stdout.write(str(alignment.accession))
							sys.stdout.write('\t')
							sys.stdout.write(str(hsp.expect))
							sys.stdout.write('\t')
							sys.stdout.write(str(hsp.score))
							sys.stdout.write('\n')
							counter+=1
	if counter==0:
		sys.stderr.write('No hits found')
		sys.stderr.write('\n')

	return 
cleaning()
