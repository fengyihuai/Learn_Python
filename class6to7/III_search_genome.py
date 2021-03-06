# -*- coding:UTF-8 -*-
# 3、在基因组序列(genome.txt)中找到转录因子
# 结合位点(TFBS.txt)；
'''In this example, the 'TFBS.txt' file contains this list of TFBSs, and
the 'genome.txt' file contains the sequence in FASTA format of, e.g.,
a whole chromosome of a eukaryotic organism of your choice.'''
import re

genome_seq = open('genome.txt').read()
# delete the '\n' in genome_seq
genome_seq = genome_seq.replace('\n', '')
# read transcription factor binding site patterns
sites = list()
for line in open('TFBS.txt'):
  fields = line.split()
  tf = fields[0]
  site = fields[1]
  sites.append((tf, site))

# match all TF's to the genome and print matches
for tf, site in sites:
    tfbs_regexp = re.compile(site)
    match_flag = tfbs_regexp.findall(genome_seq)
    matches = tfbs_regexp.finditer(genome_seq)
    # if the match_flag is empty(null), ignore the post procedures
    if match_flag:
        print(tf+':')
        for tfbs in matches:
            print('\t', tfbs.group(), tfbs.start(), tfbs.end())
