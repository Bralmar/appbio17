#!/usr/bin/env python2

from Bio import SeqIO
from Bio.Blast import NCBIXML
import sys
import re

def search():
	query=[]
	acc=[]
	exp=[]
	score=[]
	accessions=[]
	counter=0
	with open(sys.argv[1], 'rU') as fil:

    		indata=NCBIXML.parse(fil)

		for record in indata:		
			
			for alignment in record.alignments:
				
				if re.search(sys.argv[2], str(alignment)):
					
					for hsp in alignment.hsps:
					
						if hsp.expect<10**(-20):
							
							query.append(str(record.query[0:20]))
						
							acc.append(str(alignment.accession))
							
							exp.append(str(hsp.expect))
							
							score.append(str(hsp.score))
							
							counter+=1
	if counter==0:
		sys.stderr.write('No hits found')
		sys.stderr.write('\n')

	return query, acc, exp, score
query, acc, exp, score=search()


def cleaning(query, acc, exp, score):
	samequer=[]
	sameacc=[]
	sameexp=[]
	samescore=[]	
	for n in range(len(query)):
		
		if query.count(query[n])>1:		
			samequer.append(query[n])
			sameacc.append(acc[n])
			sameexp.append(exp[n])
			samescore.append(score[n])
		else:
			sys.stdout.write(query[n] + '\t' + acc[n] + '\t' + exp[n] + '\t' + score[n] + '\n')			

	
	for i in range(len(samequer)):
		if sameexp[i]==min(sameexp):
			sys.stdout.write(samequer[i] + '\t' + sameacc[i] + '\t' + sameexp[i] + '\t' + samescore[i] + '\n')


	return
cleaning(query, acc, exp, score)			
			









							
