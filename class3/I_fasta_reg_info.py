# -*- coding:UTF-8 -*-
# 把Homo sapiens且GN=‘YWHAH’的登记记录（标题行+序列行）写一个新文件

# elicit the Homo sapiens and GN=''
f = open('SwissProtSeq.fasta', 'r')
flag = 0
filter_str = "Homo sapiens GN=YWHAH"
reg_info = list()
# for line in open('SwissProtSeq.fasta'):
for line in f:
    if line[0] == '>':
        seq_str1 = line.split('OS=')
        seq_str2 = seq_str1[1].split(' PE')
        # split the strings between 'OS=' and ' PE'
        reg_initstr = seq_str2[0]
        if reg_initstr == filter_str:
            reg_info.append(line.replace('\n', ''))
            flag = 1
        else:
            flag = 0
    elif flag == 1:
        reg_info.append(line.replace('\n', ''))

print('The filtered sequence is:')
for index in range(len(reg_info)):
    print(reg_info[index])

# Open for 'w'riting
f = open('Filtered_SwissPortSeq.txt', 'w')
# Write text to file
for index in range(len(reg_info)):
    f.write("%s\n" % (reg_info[index]))
# Close the file
f.close()