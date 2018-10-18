# -*- coding:UTF-8 -*-
from urllib import request

import requests
import re
import html

def decodeHtml(input):
    # Convert all named and numeric character references
    # (e.g. &gt;, &#62;, &x3e;) in the string s to the
    # corresponding unicode characters.
    # Unicode HTML Entities are need to be converted in this exp.
    s = html.unescape(input)
    return s

url = 'http://opac.smu.edu.cn/opac/openlink.php?'
headers = {"strText": "python", "strSearchType": "title"}
res = requests.get(url, headers)

# print(res.headers['content-type'])
# print(res.content)
# print(res.text)
# res.json()
res.text
# title = re.search('<title>.{5,400}</title>', res.text, re.S)
title = re.search('<title>.{5,400}</title>', res.text, re.S)
print(title)

item = re.findall('<h3>.*</h3>', res.text)
for index in range(len(item)):
    # item_info = re.findall('1.*</a>', item[index])
    # print(decodeHtml(item_info))
    item_str = decodeHtml(item[index])
    if '>1.' in item_str:
        print('The first retrieve item is:\n'+item_str)
        book_str = re.split('</a>', item_str)[0]
        book_str = re.split('1\.', book_str)[1]
        print('This book\'s name is: ' + book_str + '\n\nOthers:')
    print(item_str)
