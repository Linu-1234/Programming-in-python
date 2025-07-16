# Hollow Rectangle
# *****
# *   *
# *   *
# *****

a = int(input('Enter no. of rows : '))
b = int(input('Enter no. of columns : '))

for i in range (0,a):
    for j in range(0,b):
        if i == 0 or i == a-1 or j == 0 or j == b-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()


# output
# Enter no. of rows : 4
# Enter no. of columns : 5
# *****
# *   *
# *   *
# *****