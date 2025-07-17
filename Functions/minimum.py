# Find maximum of three numbers

a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))
c = int(input('Enter the third number : '))

def minimum(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c
    
print(f'{minimum(a,b,c)} is the minimum number among {a},{b} and {c}.')


# output
# Enter the first number : 4
# Enter the second number : 6
# Enter the third number : 2
# 2 is the minimum number among 4,6 and 2.