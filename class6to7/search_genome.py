# -*- coding:UTF-8 -*-
import re

reg_title = list()
genome_match = list()
f1 = open('TFBS.txt', 'r')
f2 = open('genome.txt', 'r')
# get IO of genome.txt and TFBS.txt

# extract transcription factor binding site patterns
# and registration titles
for line in f1:
    reg_title.append(line.split(' ')[0])
    genome_match.append(line.split(' ')[1])


# delete the line break('\n') in text
genome_seq = f2.read().replace('\n', '')

# match all TF's to the genome and print matches
for index in range(len(genome_match)):
    print(reg_title[index], ':')
    pattern = re.compile(genome_match[index])
    match_iter = pattern.finditer(genome_seq)
    for matches in match_iter:
        print('\t', matches.group(), matches.start(), matches.end())
