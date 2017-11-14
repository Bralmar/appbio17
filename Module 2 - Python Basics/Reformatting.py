#Re-formatting Sequences
''' Takes Stockholm files as input and reformats them into fasta format files, with each line at
most 60 character long.
'''
#Main function that is used to call and ask for the input file
def main():
    filename = input("Enter filename that you want to input: ")
    return filename
filename = main()

# Function takes an input file and returns 2 lists. One list contains all seqsuences
# and one list contains all sequences.
def String_into_fasta(filename):
    seq = ("")
    species =  ("")
    workfile = open(filename, 'r')
    for Line in workfile:   #Works through each line in the inputfile
        Line = Line.split('\n',1)[0]    #Remove epmpy lines
        Line = Line.split("//",1)[0]    #Removes lines with //
        Line = Line.split("#",1)[0]     #Removes lines with #
        words = Line.split()                #Splits each line into distinct words in a list

        for i in range(0, len(words), 2): #workaround to skip empy list elements []

            if  len(words) ==2:                 #Looks at and store the seq
                seq += '\n' + words[1]

            else:
                seq += '\n' + "empty"   #If a sequence is missing it prints empy

        for i in range(0,len(words),2): #Store the 0th element in the list and store it as species
            species += '>' +  words[0] + '\n'  #+ species

    ListSeq = seq.split()   #Splits the strings into lists, used later for easier control
    ListSpecies = species.split()

    return ListSeq, ListSpecies
ListSeq, ListSpecies = String_into_fasta(filename)

#Function which will reformat the length of the sequences into fasta format,
# each line behing max 60 char
def Reformat_Length(ListSeq):
    NewList = ("")
    FragmentList = []
    for n in range(0, len(ListSeq)): #Looks at one DNA seq at the time
        WordList= ListSeq[n]        #List of words
        if len(WordList) > 60: #Lookst if the number of words in the list is more than 60
            SegWordList = list(map(' '.join, zip(*[iter(WordList)]*60))) #segments the list into words with spaces of 60
            for i in range(0, len(SegWordList)): #Iriterate of all elements in the list and adds them into a string
                NewList = NewList + SegWordList[i] +'\n'    #creates individual lines for each 60 line string
        else:
            NewList = WordList  #If the line is less than 60 char it does not have to be split into a new line

        NewList = New.replace(" ","")   #Removs the spaces which was introduced when the segments was made
        FragmentList.append(New)        #Appends all to a list
        NewList = ("")
    return FragmentList
FragmentList = Reformat_Length(ListSeq)

#For-loop which prints our output.
for n in range(0, len(ListSpecies),1):
    print(ListSpecies[n])
    print(FragmentList[n])
