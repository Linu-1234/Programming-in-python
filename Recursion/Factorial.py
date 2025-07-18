# Factorial of a number

n = int(input('Enter a number : '))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(f'The factorial of {n} is :',factorial(n))


# output
# Enter a number : 5
# The factorial of 5 is : 120