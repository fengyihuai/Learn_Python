# -*- coding:UTF-8 -*-
import re

# def name_of_email(addr):
#     # ^ \w[\w\s]+\w$
#     # addr_name = re.match(r'^([a-zA-Z\<\>\s]).*\@\w+[\.org\.com]', addr)
#     addr_name = re.match(r'([a-zA-Z\s]+|<[a-zA-Z\s]+>).*\@\w+[\.org\.com]', addr)
#     if addr_name:
#         return addr_name.groups()
#     else:
#         return None

def name_of_email(addr):
    m = re.match(r'<?(\w+\s?\w+)>?.*@\w+.\w{3}', addr)
    return m.group(1)

# test:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
assert name_of_email('bob@example.com => bob') == 'bob'
print('ok')