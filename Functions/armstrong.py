# Check if a number is Armstrong

n = int(input('Enter a number : '))

def isarmstrong(n):
    num = n
    last_digit = 0
    result = 0
    order = len(str(n))
    while n != 0:
        last_digit = n % 10
        result += last_digit ** order
        n = n // 10
    return num == result

armstrong = isarmstrong(n)

if armstrong == True:
    print(f'{n} is an armstrong number.')
else:
    print(f'{n} is not an armstrong number.')


# output
# Enter a number : 153
# 153 is an armstrong number.