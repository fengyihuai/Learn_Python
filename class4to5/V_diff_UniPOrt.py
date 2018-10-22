# -*- coding:UTF-8 -*-

f1 = open('list_new.txt', 'r')
new_str = f1.read()
new_str= new_str.replace('\n', '')
new_set = set(new_str)

f2 = open('list_old.txt', 'r')
old_str = f2.read()
old_str = old_str.replace('\n', '')
old_set = set(old_str)

diff_set = new_set - old_set
print(diff_set)