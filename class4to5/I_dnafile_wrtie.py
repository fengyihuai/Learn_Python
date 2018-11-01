# -*- coding:UTF-8 -*-
# 1、随机创建碱基序列，并进行文件读写和数据统计：
import random
from unittest import result

dna_length = 20
alphabet = 'ATGC'
dna_str = ''
for i in range(dna_length):
    dna_a = random.randint(0, 3)
    dna_str += alphabet[dna_a]

print(dna_str)

# Open for 'w'riting
f = open('randomDNA.txt', 'w')
# Write text to file
f.write(dna_str)
# Close the file
f.close()
# https://blog.csdn.net/aihali/article/details/46622251
# f = open('randomDNA.txt', 'a')

'''
从文件randomDNA.txt中读取DNA序列，
并计算每个碱基出现的频率，并将结果输出到文件resultDNA.txt
'''
f = open('randomDNA.txt', 'r')
dna_s = f.read()
print(dna_s)

index = 0
num = list()
nbase_rate = list()
# num = [0, 0, 0, 0]
# nbase_rate = [0, 0, 0, 0]
for dna_a in alphabet:
     # num[index] = dna_s.count(dna_a)
     # nbase_rate[index] = num[index]/len(dna_s)
     num.append(dna_s.count(dna_a))
     nbase_rate.append(num[index]/len(dna_s))
     index += 1

# # max_nbase = alphabet[num.index(max(num))]
# construct the text of the rate of each base pair
result = 'the rate of each nucleobase'
for index in range(len(alphabet)):
    result += '\nNbase-'
    result += alphabet[index]
    result += ' : '
    result += str(nbase_rate[index])
    result += '%'

# Open for 'w'riting
f = open('resultDNA.txt', 'w')
# Write text to file
f.write(result)
# Close the file
f.close()
