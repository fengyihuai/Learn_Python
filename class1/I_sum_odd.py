# -*- coding: UTF-8 -*-
# 1.计算从1到1000以内所有奇数的和并输出
# solution 1
sum = 0
for num in range(1,1001):
    # print(num)
    if num%2:
        sum += num

print('\nThe sum of odd integers ranging from 1 to 1000 is:', sum)

# solution 2
sum = 0
n = 1000 - 1
while n > 0:
    sum = sum + n
    n = n - 2
print('\nThe sum of odd integers ranging from 1 to 1000 is:', sum)

print()