#!/usr/bin/env python2

from Bio import SeqIO
from Bio.Blast import NCBIXML
import sys
import re
import argparse
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


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
				
					
				for hsp in alignment.hsps:
							
					score.append(hsp.score)
					
				
	if counter==0:
		sys.stderr.write('No hits found')
		sys.stderr.write('\n')

	return score, acc
score, acc = search()



def histo(score):

	plt.hist(score, normed=True, bins=30)
	#plt.xlabel('Score')
	plt.ylabel('Probability')
	plt.title('Hej')


	fig = plt.gcf()
	pp = PdfPages("hej.pdf")
	pp.savefig(fig)
	pp.close()
histo(score)





							

