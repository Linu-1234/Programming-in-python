# Print the largest of three numbers.

a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))
c = int(input('Enter the third number : '))

if a > b:
    if a > c:
        print(f'{a} is the largest number.')
    else:
        print(f'{c} is the largest number.')
else:
    if b > c:
        print(f'{b} is the largest number.')
    else:
        print(f'{c} is the largest number.')


# output
# Enter the first number : 2
# Enter the second number : 3
# Enter the third number : 4
# 4 is the largest number.