# Reverse a number

n = int(input('Enter a number : '))

def reverse(n):
    last_digit = 0
    reverse_number = 0
    while n != 0:
        last_digit = n % 10
        reverse_number = (reverse_number * 10) + last_digit
        n = n // 10
    return reverse_number

print(f'The reverse of the number {n} is :',reverse(n))


# output
# Enter a number : 123
# The reverse of the number 123 is : 321