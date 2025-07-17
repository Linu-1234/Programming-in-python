# Count the digits in a number

n = int(input('Enter the number : '))

def count(n):
    count_digit = 0
    while n != 0:
        count_digit += 1
        n = n // 10
    return count_digit

print(f'The count of the digits in {n} is :',count(n))


# output
# Enter the number : 123
# The count of the digits in 123 is : 3

