# Find the Most Frequent Character in a String.

s = input('Enter a string : ')

frequency_dict = {} #creating an empty dictionary

for char in s:
    if char in frequency_dict:
        frequency_dict[char]+=1
    else:
        frequency_dict[char]=1

print('Character Frequency:')
for char,count in frequency_dict.items():
    print(f'{char}:{count}')

max_frequency = max(frequency_dict.values())
most_frequent_characters = [char for char,count in frequency_dict.items() if count == max_frequency]

print('Most Occuring Characters:')
for char in most_frequent_characters:
    print(f'{char} occurs {max_frequency} times.')



# output
# Enter a string : priyambada
# Character Frequency:
# p:1
# r:1
# i:1
# y:1
# a:3
# m:1
# b:1
# d:1
# Most Occuring Characters:
# a occurs 3 times.
