#  Inverted Triangle
# ****
# ***
# **
# *

n = int(input('Enter no. of rows : '))

for i in range(0,n):
    for j in range(0,n-i):
        print('*',end='')
    print()


# output
# Enter no. of rows : 4
# ****
# ***
# **
# *