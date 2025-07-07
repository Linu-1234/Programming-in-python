# Remove Duplicates from a String.

s = input('Enter a string : ')
result = []
for char in s:
    if char not in result:
        result.append(char)
string = "".join(result)
    
print('The string after removing duplicates is : ',string)



# output 
# Enter a string : programming
# The string after removing duplicates is :  progamin