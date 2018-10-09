# -*- coding:UTF-8 -*-
# 2、读取Fasta格式文件，提取登记码并打印输出；并把Homo sapiens
# 且GN=‘YWHAH’的登记记录（标题行+序列行）写一个新文件

f = open('SwissProtSeq.fasta', 'r')
id_str = list()
# for line in open('SwissProtSeq.fasta'):
for line in f:
    if line[0] == '>':
        # id_str.append(str(line[4:10]))
        seq_str = line.split('|')
        id_str.append(seq_str[1])
print(id_str)

# Open for 'w'riting
f = open('IDofSwissProtSeq.txt', 'w')
# Write text to file
for index in range(len(id_str)):
    f.write("%s\n"%(id_str[index]))
# Close the file
f.close()

