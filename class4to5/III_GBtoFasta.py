# -*- coding:UTF-8 -*-

f = open('AY810830.gb', 'r')
mark = "ACCESSION"
DNA_M = "ORIGIN"
flag = False
dna_seq = list()

for line in f:
    if flag == False:
        if mark in line:
            ID = line[len(mark):]
            ID.replace('\n', '')
            ID = ''.join(ID.split())
            ID = '>sp|'+ID+'|'
        elif DNA_M in line:
            flag = True
            continue
    elif line[0:1] != '\\' and flag == True:
        dna_str = line[10:65].upper()
        dna_str = ''.join(dna_str.split())
        dna_str.upper()
        dna_seq.append(dna_str)

# Open for 'w'riting
f = open('output.fasta', 'w')
f.write("%s\n"%(ID))
# Write text to file
for index in range(len(dna_seq)):
    f.write("%s\n" % (dna_seq[index]))
# Close the file
f.close()
