# Check if a number is Perfect Square or not

n = int(input('Enter a number : '))

def isperfectsquare(n):
    return (n ** 0.5) ** 2 == n

perfect_square = isperfectsquare(n)

if perfect_square == True:
    print(f'{n} is a perfect square.')
else:
    print(f'{n} is not a perfect square.')


# output
# Enter a number : 25
# 25 is a perfect square.

