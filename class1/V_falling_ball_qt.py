# -*- coding: UTF-8 -*-
# 5.一球从100米高度自由落下，每次落地后反跳回原高度的一半，
# 再落下。求它在第n次落地时，共经过多少米？

# strategy A
n = int(input('The n_th time the ball landed，n='))
Sn = 100.0  # The road passed on the first landing
Hn = Sn / 2 # The road passed on the second landing

if n != 1:
    for i in range(1, n):
        Sn += 2 * Hn    # The falling height at each landing
        # is half of the previous falling height
        Hn /= 2

print('Total of road is %0.2f m' % Sn)

# strategy B
print()
num_v = int(input('The n_th time the ball landed，n='))
num191 = 100
sum191 = -100
num192 = 0
while num192 >= 0:
    sum191 = sum191 + num191 * 2
    num191 = num191 / 2
    num192 += 1
    if num192 == num_v:
        print('n={}, road={}m'.format(num192, sum191))
        break