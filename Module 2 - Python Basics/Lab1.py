import random
x = int(input("Choose your DNA length"))
i = 0
seq = ""
for i in range (1, x):
    i = i+1
    nuc = random.choice("ATCG")
    seq = seq + nuc
print("myseq")
print(seq)
