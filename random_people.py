# -*- coding:UTF-8 -*-
import random

# work_num = input("本次作业题数：")
work_num = 4
names = ['zou', 'li', 'huang', 'liu']

work_assign = names
# names sequence is permuted pseudo_randomly
random.shuffle(work_assign)

if work_num > len(names):
    addition = random.randint(0,len(names)-1)
    # Random additions
    work_assign.append(addition)

for index in range(len(work_assign)):
    print("题目", index+1, "：", work_assign[index])