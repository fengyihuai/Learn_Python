# -*- coding: UTF-8 -*-
# 4.输出最小的3个3位水仙花数
# style 1
print('The three smallest 3-digit narcissistic number are:')
# 最小的三个3位水仙花数位
nmin = 3
for num in range(100, 1000):
    sum=0
    temp=num
    while temp:
        sum=sum+(temp%10)**3
        temp//=10
    if sum==num:
        print(num)
        nmin -= 1
    if nmin == 0:
        break

# style 2
print()
limit = 3
for i in range(100, 1000):
    num1 = i // 100
    num2 = i // 10 % 10
    num3 = i % 10
    num = num1**3 + num2**3 + num3**3
    if num==i and limit>0:
        print (i)
        limit -= 1