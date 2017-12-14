#!/usr/bin/env python2

from Bio import SeqIO
from Bio.Blast import NCBIXML
import sys
import re
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import argparse
from matplotlib.backends.backend_pdf import PdfPages





def search(args):
	query=[]
	Numb=[]
	score=[]
	counter=0
	
	with open(args.filename) as file:

    		indata=NCBIXML.parse(file)

		for record in indata:
		
			for alignment in record.alignments:
			
				for hsp in alignment.hsps:

					query.append(record.query)

					if record.query==query[0]:
						counter+=1
						score.append(hsp.score)
						Numb.append(counter)
															
	return score, Numb, query


def histo(score, acc, query, args):

	plt.bar(acc, score)
	plt.xlabel('Hit number')
	plt.ylabel('Score')
	plt.title(query[0])


	fig = plt.gcf()
	pp = PdfPages(args.output)
	pp.savefig(fig)
	pp.close()
	
	return 


def Main():
	parser = argparse.ArgumentParser() 
	parser.add_argument("filename", help = "input filename") 
	parser.add_argument("output", help="output filename")
	args=parser.parse_args()
	output = args.output	
	score, acc, query=search(args)
	plot= histo(score, acc, query, args)

	
	return


Main()
