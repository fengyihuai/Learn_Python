# -*- coding: UTF-8 -*-
# 7.随机生成一个DNA序列，统计4种碱基出现的频率，并给出
# 本序列中出现频率最高的碱基
# from random import choice
import random

def dna_string(length):
    DNA = ""
    for count in range(length):
        # DNA += choice("CGTA")
        DNA += random.choice("CGTA")
    return DNA

def dna_string2(length):
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

seq_length = 20
dna_str = dna_string(seq_length)
print('DNA Sequence:', dna_str)
base_list = ['C', 'G', 'T', 'A']
# list_DNA = "CGTA"
num_DNA = [0, 0, 0, 0]
index = 0
for s in 'CGTA':
    num_DNA[index] = dna_str.count(s)
    index += 1

max_dna_str = base_list[num_DNA.index(max(num_DNA))]

for index in range(0, 4):
    print('number of {} is {}'.format(base_list[index], num_DNA[index]))
print('\nThe maximum is {}'.format(max_dna_str))

print()