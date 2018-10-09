# -*- coding: UTF-8 -*-
# 6.打印出一个九九乘法表，要求每个等式上下对齐
for i in range(1, 10):
    for j in range(1, i+1):
        print('{0}x{1}={2}'.format(j, i, i*j), end='\t')
        # print('\t{}x{}={}'.format(j, i, i*j), end='')
        # print(j, '*', i, '=', i*j, sep='',end=' ')
    print()

print()