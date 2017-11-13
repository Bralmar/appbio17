#Re-formatting Sequences
def main():
    filename = input("Enter filename that you want to input: ")
    return filename
filename = main()


def String_into_fasta(filename):
    seq = ("")
    species =  ("")
    workfile = open(filename, 'r')
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
ListSeq, ListSpecies = String_into_fasta(filename)

def Reformat_Length(ListSeq):
    New = ("")
    FragList = []
    for n in range(0, len(ListSeq)): #Looks at one DNA seq at the time
        WordList= ListSeq[n]
        if len(WordList) > 10: #Lookst if the number of words in the list is more than 10
            SegWordList = list(map(' '.join, zip(*[iter(WordList)]*10))) #segments the list into words with spaces of 10
            for i in range(0, len(SegWordList)):
                New = New + SegWordList[i] +'\n'
        New = New.replace(" ","")
        FragList.append(New)
        New = ("")
    return FragList
FragList = Reformat_Length(ListSeq)

for n in range(0, len(ListSpecies),1):
    print(ListSpecies[n])
    print(FragList[n])
