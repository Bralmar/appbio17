#Re-formatting Sequences
def String_into_fasta():
    filename = input("Enter filename that you want to input: ")
    workfile = open(filename, 'r')
    seq = ("")
    species =  ("")

    for Line in workfile:
        Line = Line.split('\n',1)[0]
        Line = Line.split("//",1)[0]
        Line = Line.split("#",1)[0]
        words = Line.split()

        for i in range(0, len(words), 2):
            seq = seq + '\n' + words[1]

        for i in range(0,len(words),2):
            species = '>' +  words[0] + '\n'  + species

    ListSeq = seq.split()
    ListSpecies = species.split()

    return ListSeq, ListSpecies

ListSeq, ListSpecies = String_into_fasta()

def Reformat_Length(ListSeq, ListSpecies):


    return

Reformat_Length(ListSeq, ListSpecies)
