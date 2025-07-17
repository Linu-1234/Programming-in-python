# Find GCD of two numbers

a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))

def GCD(a,b):
    while b != 0:
        a,b = b,a%b #Euclidean algorithm 
    return a

print(f'The GCD of {a} and {b} is :',GCD(a,b))


# output
# Enter the first number : 48
# Enter the second number : 60
# The GCD of 48 and 60 is : 12