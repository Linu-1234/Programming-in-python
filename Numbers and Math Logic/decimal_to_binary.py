# Convert Decimal to Binary

decimal = int(input('Enter the decimal number : '))

if decimal == 0:
    print(f'The binary number of {decimal} is : 0')
else:
    n = decimal
    binary = ''
    while n != 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    print(f'The binary number of {decimal} is :',binary)

# output
# Enter the decimal number : 4
# The binary number of 4 is : 100