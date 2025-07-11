# Convert Binary to Decimal

binary = input('Enter a binary number : ')

power = len(binary) - 1
decimal = 0

for i in binary:
    decimal += int(i) * (2 ** power)
    power -= 1

print(f'The decimal number of {binary} is :',decimal)


# output
# Enter a binary number : 100
# The decimal number of 100 is : 4

