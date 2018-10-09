# -*- coding: UTF-8 -*-
# 7.随机生成一个DNA序列，统计4种碱基出现的频率，并给出
# 本序列中出现频率最高的碱基
# from random import choice
import random

def DNAString(length):
    DNA = ""
    for count in range(length):
        # DNA += choice("CGTA")
        DNA += random.choice("CGTA")
    return DNA

def DNAString2(length):
    DNA = ""
    for inum in range(0,4):
        t = random.randint(1,4)
        if t == 1:
            DNA += 'C'
        elif t == 2:
            DNA += 'G'
        elif t == 3:
            DNA += 'T'
        else:
            DNA += 'A'
    return DNA

num_seq = 20
dna_str = DNAString(num_seq)
print('DNA Sequence:',dna_str)
list_DNA = ['C', 'G', 'T', 'A']
num_DNA = [0, 0, 0, 0]
i = 0;
for s in 'CGTA':
    num_DNA[i] = dna_str.count(s)
    i += 1

max_dna_str = list_DNA[num_DNA.index(max(num_DNA))]

for i in range(0, 4):
    print('number of {} is {}'.format(list_DNA[i], num_DNA[i]))
print('\nThe maximum is {}'.format(max_dna_str))

print()