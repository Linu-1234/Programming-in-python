# Check if a string is a palindrome

str = input('Enter the string : ')

def ispallindrome(str):
    reverse = str[::-1]
    return reverse == str

pallindrome = ispallindrome(str)

if pallindrome == True:
    print(f'{str} is pallindrome.')
else:
    print(f'{str} is not pallindrome.')


# output
# Enter the string : eye
# eye is pallindrome.