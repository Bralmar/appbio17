import random
import pdb
x = int(input("Choose your DNA length"))
i = 0
seq = ""

for i in range (1, x):
    i = i+1

    nuc = random.choice("ATCG")
    pdb.set_trace()
    seq = seq + nuc
print("myseq")
print(seq)
