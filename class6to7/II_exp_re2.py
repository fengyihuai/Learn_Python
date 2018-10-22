# -*- coding:UTF-8 -*-
import re

separator = re.compile('\|')

# split
annotation = 'ATOM:CA|RES:ALA|CHAIN:B|NUMRES:166'
columns = separator.split(annotation)
print(columns)

# replace
new_annotation = (separator.sub('@', annotation))
print(new_annotation)

new_annotation2 = separator.sub('@', annotation)
print(new_annotation2)
