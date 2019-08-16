# -*- coding: UTF-8 -*-
#3.输出10行内容，每行的内容都是"******"
# for-flow style
for ilist in [1, 2, 3, 4]:
    print('*'*ilist)

print('The for loop is over.\n')

for ilist in [1, 3, 5, 3, 1]:
    print('{0: ^5}'.format('*'*ilist))

print('The for loop is over.\n')

for ilist in range(10):
    print('******')
print('The for loop is over.\n')

# while-flow style
irow = nrow = 4
while irow > 0:
    print('*' * (nrow-irow+1))
    irow -= 1
else:
    print('The while loop is over.\n')
    # Do anything else you want to do here

irow = 1
while irow < 5:
    print('*' * (irow))
    irow += 1
else:
    print('The while loop is over.\n')


irow = nrow = 5
list = [1, 3, 5, 3, 1]
while irow > 0:
    print('{0: ^5}'.format('*' * list[nrow-irow]))
    irow -= 1
else:
    print('The while loop is over.\n')
    # Do anything else you want to do here

irow = 1
list = [1, 3, 5, 3, 1]
while irow < 6:
    print('{0: ^5}'.format('*' * list[irow-1]))
    irow += 1
else:
    print('THe while loop is over.\n')
    # Do anythong else you want to do here

print()