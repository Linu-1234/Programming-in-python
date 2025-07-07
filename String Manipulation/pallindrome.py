# Check if a String is a Palindrome

string = input('Enter a string : ')
reverse_string = string[::-1]

if string == reverse_string:
    print('The string is pallindrome.')
else:
    print('The string is not pallindrome.')



# output
# Enter a string : madam
# The string is pallindrome.