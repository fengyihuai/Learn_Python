# -*- coding:UTF-8 -*-
# 3、从GenBank格式文件中提取登记码ACCESSION ，
# 并将核苷酸序列写入一个Fasta格式的新文件中；
f = open('AY810830.gb', 'r')
# check = f.readlines()
mark = "ACCESSION"
DNA_M = "ORIGIN"
flag = False
dna_seq = list()
for line in f:
    if flag == False:
        if mark in line:
            # ID = line[len(mark):]
            # ID.replace('\n', '')
            # ID = ''.join(ID.split())
            ID = line.split()[1]
            ID = '>sp|'+ID+'|'
        elif DNA_M in line:
            flag = True
    elif line[0:1] != '\\' and flag == True:
        # dna_str = line[10:65].upper()
        # merge the list to str
        # dna_str = ''.join(dna_str.split())
        dna_str = ''.join(line.split()[1:])
        # Return a copy of str converted to uppercase
        dna_seq.append(dna_str.upper())

# Open for 'w'riting
f = open('output.fasta', 'w')
f.write("%s\n"%(ID))
# Write text to file
for index in range(len(dna_seq)):
    f.write("%s\n" % (dna_seq[index]))
# Close the file
f.close()
