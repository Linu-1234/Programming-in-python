# implementation of selection sort

array = list(map(int,input('Enter the elements of array separated by space : ').split()))

n  = len(array)

for i in range(0,n):
    min_index = i
    for j in range(i+1,n):
        if array[j] < array[min_index]:
            min_index = j
    array[i] , array[min_index] = array[min_index] , array[i]

print('The array after sorting is :',array)