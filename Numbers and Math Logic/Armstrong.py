# Check for Armstrong number.

n = int(input('Enter a number : '))

num = n
order = len(str(n))
last_digit = 0
sum = 0

while n != 0:
    last_digit = n % 10
    sum +=  last_digit ** order
    n = n // 10

if num == sum:
    print(f'{num} is an armstrong number.')
else:
    print(f'{num} is not an armstrong number.')


# output
# Enter a number : 153
# 153 is an armstrong number.