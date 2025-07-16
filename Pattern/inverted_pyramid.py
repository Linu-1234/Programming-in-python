# Inverted Pyramid
# *******
#  *****
#   ***
#    *

n = int(input('Enter no. of rows : ')) 

a = 0
b = n
for i in range(1,n+1):
    for j in range(0,a):
        print(' ',end='')
    for k in range(0,2*b-1):
        print('*',end='')
    a += 1
    b -= 1
    print()


# output
# Enter no. of rows : 4
# *******
#  *****
#   ***
#    *