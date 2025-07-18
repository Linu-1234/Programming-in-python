# Reverse a string

str = input('Enter a string : ')

def reverse(str):
    if len(str) == 0:
        return ""
    else:
        return reverse(str[1:]) + str[0]
    
print(f'The reverse of the string {str} is :',reverse(str))


# output
# Enter a string : lina
# The reverse of the string lina is : anil