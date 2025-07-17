# Check if a number is Strong

n = int(input('Enter a number : '))

def factorial(a):
    fact = 1
    for i in range(2,a+1):
        fact *= i
    return fact

def isstrong(n):
    num = n
    last_digit = 0
    result = 0
    while n != 0:
        last_digit = n % 10
        result += factorial(last_digit)
        n = n // 10
    return num == result

strong = isstrong(n)

if strong == True:
    print(f'{n} is a strong number.')
else:
    print(f'{n} is not a strong number.')


# output
# Enter a number : 145
# 145 is a strong number.
