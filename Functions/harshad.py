# Check if a number is a Harshad number
# Number divisible by the sum of its digits (e.g., 18 → 1+8 = 9 → 18 % 9 = 0)

n = int(input('Enter a number : '))

def isharshad(n):
    num = n
    last_digit = 0
    sum = 0
    while n != 0:
        last_digit = n % 10
        sum += last_digit
        n = n // 10
    return num % sum

harshad = isharshad(n)
if harshad == 0:
    print(f'{n} is a harshad number.')
else:
    print(f'{n} is not a harshad number.')


# output
# Enter a number : 18
# 18 is a harshad number.