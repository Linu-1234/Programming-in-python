# Sum of digits of a number

n = int(input('Enter the number : '))

def sum(n):
    sum = 0
    last_digit = 0
    while n != 0:
        last_digit = n % 10
        sum += last_digit
        n = n // 10
    return sum

print(f'The sum of the digits of {n} is :',sum(n))


# output
# Enter the number : 123
# The sum of the digits of 123 is : 6