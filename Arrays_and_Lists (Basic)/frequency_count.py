# Count the frequency of each element

array = list(map(int,input('Enter numbers separated by space : ').split()))

frequency = {}

for num in array:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num , count in frequency.items():
    print(f'{num} : {count}')


# output
# Enter numbers separated by space : 1 3 4 5 2 3 4 1 1
# 1 : 3
# 3 : 2
# 4 : 2
# 5 : 1
# 2 : 1