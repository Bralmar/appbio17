# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:44:17 2017

@author: Emil
"""

def extract_sequence():
    raw=input('Which file? ')
    file=open(raw, 'r')
    sequence=[]
    name=[]
    joined=[]
    for line in file:
        if line.startswith('>'):
            name.append(line.split())
            joined.append(sequence)
        else:
            sequence.append(line)    
    return sequence, name
sequence=extract_sequence()
print(sequence)


def join_lines(sequence):
    joinedsequence=[]
    for line in sequence:
        joinedsequence.append(line.replace('\n',''))
        return joinedsequence
joinedsequence=join_lines(sequence)
print(joinedsequence)







#def find_ORF(seqstr)
#orfs=[]
#allorfs=[]   
#for i in range(0, len(seqstr), 3):
    #codon = seqstr[i:i+3]
    #orf.append(codon)
   # if codon == "TAA" or codon == "TGA" or codon == "TAG":
       # orfs=''.join(orf)
       # allorfs.append(orfs)
       # orf=[]
#orf = seqstr[:i+3]
#orfs.append(orf)
#orf =[]   
    #return orf
#orf=find_ORF(seqstr)
#print(orfs)
