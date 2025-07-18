# GCD using recursion

a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))

def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b,a%b)
    
print(f'The GCD of {a} and {b} is :',GCD(a,b))