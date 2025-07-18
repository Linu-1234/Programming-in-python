# Sum of first N natural numbers

n = int(input('Enter the value of n : '))

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
print(f'The sum of first {n} natural numbers is :',sum(n))


# output
# Enter the value of n : 5
# The sum of first 5 natural numbers is : 15