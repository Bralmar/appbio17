#!/usr/bin/env python2

from Bio import SeqIO
from Bio.Blast import NCBIXML
import sys
import re
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import argparse
from matplotlib.backends.backend_pdf import PdfPages


#parser=argparse.ArgumentParser(description='Create a beautiful diagram of your BLAST search')
#parser.add_argument("a")
#parser.add_argument('a', nargs='?', default="check_empty")
#args=parser.parse_args()



def search():
	query=[]
	Numb=[]
	score=[]
	counter=0
	with open(sys.argv[1], 'rU') as fil:

    		indata=NCBIXML.parse(fil)

		for record in indata:
		
			for alignment in record.alignments:
			
				for hsp in alignment.hsps:

					query.append(record.query)

					if record.query==query[0]:
						counter+=1
						score.append(hsp.score)
						Numb.append(counter)
															
	return score, Numb, query
score, acc, query=search()

def histo(score, acc, query):

	plt.bar(acc, score)
	plt.xlabel('Hit number')
	plt.ylabel('Score')
	plt.title(query[0])


	fig = plt.gcf()
	pp = PdfPages("hej.pdf")
	pp.savefig(fig)
	pp.close()
histo(score, acc, query)

