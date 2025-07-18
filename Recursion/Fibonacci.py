# Fibonacci series

n = int(input('Enter the term : '))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(f'The {n}th fibonacci term is :',fibonacci(n))


# output
# Enter the term : 3
# The 3th fibonacci term is : 2