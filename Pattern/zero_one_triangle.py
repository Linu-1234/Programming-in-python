#  0-1 Triangle
# 1
# 0 1
# 1 0 1
# 0 1 0 1

n = int(input('Enter no. of rows : '))

for i in range(1,n+1):
    for j in range(1,i+1):
        if i % 2 != 0:
            if j % 2 != 0 :
                print('1',end=' ')
            else:
                print('0',end=' ')
        else:
            if j % 2 != 0:
                print('0',end=' ')
            else:
                print('1',end=' ')
    print()


# output
# Enter no. of rows : 4
# 1
# 0 1
# 1 0 1
# 0 1 0 1

