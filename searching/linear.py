# Implementation of linear search

array = list(map(int,input('Enter the elements of array separated by space :').split()))
target = int(input('Enter the element to be searched : '))


def linear_search(array,target):
    for i in range(0,len(array)):
        if array[i] == target:
            return i
    return -1
        

index = linear_search(array,target)

if index != -1:
    print(f'The target element {target} present at index {index}.')
else:
    print('Element not found.')


# output
# Enter the elements of array separated by space :1 5 3 7 2 1
# Enter the element to be searched : 1
# The target element 1 present at index 0.
