# Find LCM of two numbers

a = int(input('Enter the first number : ')) 
b = int(input('Enter the second number : '))

def GCD(a,b):
    while b != 0:
        a ,b = b, a % b
    return a

def LCM(a,b):
    return (a * b) // GCD(a,b)

print(f'The LCM of {a} and {b} is :',LCM(a,b))


# output
# Enter the first number :12
# Enter the second number : 36
# The LCM of 12 and 36 is : 36