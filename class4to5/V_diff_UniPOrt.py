# -*- coding:UTF-8 -*-
# 5、比较不同版本的UniProt数据库文件的差异。

f_new = open('list_new.txt', 'r')
new_str = f_new.read()
new_str= new_str.replace('\n', '')
new_set = set(new_str)

f_old = open('list_old.txt', 'r')
old_str = f_old.read()
old_str = old_str.replace('\n', '')
old_set = set(old_str)
# go back to file header
# f_old.seek(0)

diff_set = new_set - old_set
print("The difference between these two files:\n",
      '\t'.join(diff_set))