# Power of a number (x^y)

x = int(input('Enter the base : '))
y = int(input('Enter the power : '))

def power(x,y):
    if y == 0:
        return 1
    else:
        return x * power(x,y-1)
    
print(f'{x} to the power {y} is :',power(x,y))


# output
# Enter the base : 2
# Enter the power : 3
# 2 to the power 3 is : 8