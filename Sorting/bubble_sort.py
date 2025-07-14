# Implementation of bubble sort 

array = list(map(int,input('Enter the elements of array separated by space : ').split()))

n = len(array)

for i in range(0,n):
    for j in range(0,n-i-1):
        if array[j] > array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]

print('The Sorted array is :',array)


# output
# Enter the elements of array separated by space : 3 6 2 7 5
# The Sorted array is : [2, 3, 5, 6, 7]
            