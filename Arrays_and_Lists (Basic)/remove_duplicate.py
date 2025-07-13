# Remove duplicates from an array

array = list(map(int,input("Enter numbers separated by space : ").split()))

seen = set()
unique = []

for i in array:
    if i not in seen:
        seen.add(i)
        unique.append(i)


print('Array after removing duplicates is :',unique)


# output
# Enter numbers separated by space : 1 4 2 6 4 3 2 1
# Array after removing duplicates is : [1, 4, 2, 6, 3]
