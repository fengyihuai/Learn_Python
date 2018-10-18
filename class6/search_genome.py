# -*- coding:UTF-8 -*-
import re

reg_title = list()
match = list()
f1 = open('TFBS.txt', 'r')
f2 = open('genome.txt', 'r')
for line in f1:
    reg_title.append(line.split(' ')[0])
    match.append(line.split(' ')[1])


genome_lines = f2.readlines()
for index in range(len(match)):
    print('\n'+reg_title[index]+':')
    pattern = re.compile(match[index])
    row_id = 0
    for line in genome_lines:
        match_iter = pattern.finditer(line)
        for matches in match_iter:
            start_id = matches.start()+row_id
            end_id = matches.end()+row_id
            row_id += len(line.strip('\n'))
            print(matches.group(), matches.span())
            # print(start_id, end_id)
            print(matches.start(), matches.end())