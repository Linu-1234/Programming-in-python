# Check if two strings are anagrams

str1 = input('Enter the first string : ')
str2 = input('Enter the second string : ')

def isanagram(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    return sorted(str1) == sorted(str2)

if isanagram(str1,str2):
    print('The two strings are anagram.')
else:
    print('The two strings are not anagram.')