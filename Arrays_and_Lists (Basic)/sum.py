# Sum of elements in an array

array = list(map(int,input('Enter numbers separated by space : ').split()))

sum = 0
for i in array:
    sum += i

print('The sum of the elements of the array is :',sum)


# output
# Enter numbers separated by space : 4 6 3 1 4
# The sum of the elements of the array is : 18