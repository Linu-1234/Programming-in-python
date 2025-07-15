# implementation of binary search

array = list(map(int,input('Enter the elements of array separated by space : ').split()))
target = int(input('Enter the element to be searched : '))


def binary_search(array,target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


index = binary_search(array,target)

if index != -1:
    print(f'The element {target} present at index {index}.')
else:
    print('Element not found.')


# output
# Enter the elements of array separated by space : 1 2 3 4 5
# Enter the element to be searched : 2
# The element 2 present at index 1.

