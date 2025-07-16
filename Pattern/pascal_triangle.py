# Pascal’s Triangle
# 1
# 1 1
# 1 2 1
# 1 3 3 1
from math import comb
n = int(input('Enter no. of rows : '))

for i in range(0,n):
    for j in range(0,i+1):
        print(comb(i,j),end=' ')
    print()