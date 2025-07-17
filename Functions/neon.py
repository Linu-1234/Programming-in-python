# Check if a number is a Neon number
# Square of number → sum of digits = number (e.g., 9 → 9² = 81 → 8+1 = 9)

n = int(input('Enter a number : '))

def isneon(n):
    square = n ** 2
    last_digit = 0
    sum = 0
    while square != 0:
        last_digit = square % 10
        sum += last_digit
        square = square // 10
    return n == sum

neon = isneon(n)
if neon == True:
    print(f'{n} is a neon number.')
else:
    print(f'{n} is not a neon number.')