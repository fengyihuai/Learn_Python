# -*- coding: UTF-8 -*-
# 4.输出最小的3个3位水仙花数
'''
在数论中，水仙花数（Narcissistic number），也被称为超完全数字不变数
（pluperfect digital invariant, PPDI）[3]、自恋数、自幂数、阿姆
斯壮数或阿姆斯特朗数（Armstrong number）[4] ，用来描述一个N位非负整
数，其各位数字的N次方和等于该数本身。

https://zh.wikipedia.org/wiki/%E6%B0%B4%E4%BB%99%E8%8A%B1%E6%95%B0
'''

# solution 1
print('The three smallest 3-digit narcissistic number are:')
# 最小的三个3位水仙花数位
nmin = 3
for num in range(100, 1000):
    sum = 0
    temp = num
    while temp:
        sum = sum + (temp % 10)**3
        temp //= 10
    if sum == num:
        print(num)
        nmin -= 1
    if nmin == 0:
        break

# solution 2
print()
limit = 3
for i in range(100, 1000):
    num1 = i // 100
    num2 = i // 10 % 10
    num3 = i % 10
    num = num1**3 + num2**3 + num3**3
    if num == i and limit > 0:
        print (i)
        limit -= 1