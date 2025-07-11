# Sum of digits of a number.

n = int(input('Enter a number : '))

num = n
sum = 0

while n != 0:
    last_digit = n % 10
    sum += last_digit
    n = n // 10

print(f'The sum of digits of {num} is :',sum)


# output
# Enter a number : 15
# The sum of digits of 15 is : 6