# Print numbers from N to 1 and 1 to N

n = int(input('Enter the value of n : '))

def descending(n):
    if n == 0:
        return
    else:
        print(n,end='')
        descending(n-1)

def ascending(n,i=1):
    if i > n:
        return
    else:
        print(i,end='')
        ascending(n,i+1)

print('Descending numbers : ')
descending(n)

print('\nAscending numbers : ')
ascending(n)



# output
# Enter the value of n : 5
# Descending numbers :
# 54321
# Ascending numbers :
# 12345