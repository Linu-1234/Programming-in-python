# Count Vowels and Consonants in a String.

s = input('Enter a string : ')
vowel = 0
consonent = 0
 
for i in s:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        vowel+=1
    else:
        consonent+=1

print(f'The no. of vowels present in {s} is : ',vowel)
print(f'The no. of consonents present in {s} is : ',consonent)



# output
# Enter a string : python
# The no. of vowels present in python is :  1
# The no. of consonents present in python is :  5