# Count vowels and consonants in a string

str = input('Enter the string : ')

def count(str):
    string = str.lower()
    vowel = 0
    consonant = 0
    for i in string:
        if i.isalpha():
            if i in ['a','e','i','o','u']:
                vowel += 1
            else:
                consonant += 1

    return vowel, consonant

vowel_count , consonant_count = count(str)

print(f'The no. of vowels in the string {str} is {vowel_count} and no. of consonants in the string {str} is {consonant_count}.')