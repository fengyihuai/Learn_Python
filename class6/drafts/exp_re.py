# -*- coding:UTF-8 -*-
import re

pattern = re.compile('R.[ST][^P]')
seq = 'RQSAMGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQRPSK P'

# findall returns a list of all matches
matches = pattern.findall(seq)
print(matches)

# finditer returns an iterator of match objects
match_iter = pattern.finditer(seq)
for match in match_iter:
    print(match.group(), match.span())
    print(match.start(), match.end())

