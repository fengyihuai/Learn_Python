# -*- coding:UTF-8 -*-
# 4、读取Fasta文件的RNA序列，并将每三个字符翻译
# 替换为一个对应的氨基酸，并打印在屏幕上；

condon_label = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

f = open('A06662-RNA.fasta', 'r')
rna_line = list()
line_list = list()
i = 0
for line in f:
    if line[0] == '>':
        headerline = line
    else:
        line_list.append(line.replace('\n', ''))
line_str = "".join(line_list)

for index in range(0, len(line_str), 3):
    # line[index:index+3]
    dict_key = "".join(line_str[index:index+3])
    rp_key = condon_label[dict_key]
    if rp_key == "STOP":
        rp_key = '*'
    rna_line.append(rp_key)
# insert the '\n' in the step of 60 alphabets
raw_step = 60
for index in range(raw_step, raw_step*len(rna_line)//raw_step, raw_step):
    rna_line.insert(index, '\n')
rna_seq = "".join(rna_line)
f.close()
print(headerline+rna_seq)

# Open for 'w'riting
f = open('amino_acid.fasta', 'w')
f.write(headerline)
# Write text to file
f.write(rna_seq)
# Close the file
f.close()