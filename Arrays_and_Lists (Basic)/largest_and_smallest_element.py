# Find the largest and smallest elements in an array.

array = list(map(int,input('Enter numbers separated by space : ').split()))

if len(array) == 0:
    print('The array is empty.')
else:
    largest = array[0]
    smallest = array[0]

    for i in array:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i

print(f'The largest element in the array is :',largest)
print(f'The smallest element in the array is :',smallest)


# output
# Enter numbers separated by space : 5 7 2 10 2 1 
# The largest element in the array is : 10
# The smallest element in the array is : 1