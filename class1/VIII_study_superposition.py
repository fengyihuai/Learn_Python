# -*- coding: UTF-8 -*-
# 8.基数为1.0，每天进步1%，一年能进步多少？反过来呢？
num_base = 1.0
days_year = 365

gain = 0.01
loss = -gain

improv = num_base * (1 + gain)**days_year
degene = num_base * (1 + loss)**days_year

print('\nThe improvement of studying everyday is {0:.2f}(one year)'.format(improv))
print('The degeneracy of giving up studying everyday is {0:.5f}(one year)'.format(degene))

print()