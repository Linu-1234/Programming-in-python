# Find the factorial of a number.

n = int(input('Enter a number : '))

fact = 1
if n < 0:
    print('Enter a positive number.')
elif n == 0:
    print('The factorial of 0 is : 1')
else:
    for i in range(2,n+1):
        fact *= i
    print(f'The factorial of {n} is :',fact)

# output 
# Enter a number : 5
# The factorial of 5 is : 120