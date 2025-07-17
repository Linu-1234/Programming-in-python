# Check if a number is palindrome

n = int(input('Enter a number : '))

def ispallindrome(n):
    num = n
    last_digit = 0
    reverse_number = 0
    while n != 0:
        last_digit = n % 10
        reverse_number = (reverse_number * 10) + last_digit
        n = n // 10
    return reverse_number == num

pallindrome = ispallindrome(n)

if pallindrome == True:
    print(f'{n} is a pallindrome number.')
else:
    print(f'{n} is not a pallindrome number.')



# output
# Enter a number : 111
# 111 is a pallindrome number.