# Implementation of insertion sort 

array = list(map(int,input('Enter elements of the array separated by space : ').split()))

n = len(array)

for i in range(1,n):
    key = array[i]
    j = i - 1

    while j >= 0 and array[j] > key :
        array[j+1] = array[j]
        j -=1

    array[j+1] = key

print('The array after sorting is :',array)


# output
# Enter elements of the array separated by space : 3 1 5 2 6
# The array after sorting is : [1, 2, 3, 5, 6]


