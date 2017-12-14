#!/usr/bin/env python2

from Bio import SeqIO
from Bio.Blast import NCBIXML
import sys
import re
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import argparse
from matplotlib.backends.backend_pdf import PdfPages


parser=argparse.ArgumentParser(description='Create a beautiful diagram of your BLAST search')
#parser.add_argument("a")
parser.add_argument('a', nargs='?', default="check_empty")
args=parser.parse_args()



def search():
	query=[]
	score=[]
	counter=0
	with open(sys.argv[1], 'rU') as fil:

    		indata=NCBIXML.parse(fil)

		for record in indata:
		
			for alignment in record.alignments:
			
				for hsp in alignment.hsps:

					query.append(record.query)

					if record.query==query[0]:

						score.append(hsp.score)
						
								
								
	return score, query
score, query=search()

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

