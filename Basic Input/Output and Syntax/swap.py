# Swap two numbers without using a third variable.

a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))

# Before swapping
print('The value of a before swapping is : ',a)
print('The value of b before swapping is : ',b)

a = a + b
b = a - b
a = a - b

# After Swapping

print('The value of a after swapping is : ',a)
print('The value of b after swapping is : ',b)


# Output
# Enter the first number : 2
# Enter the second number : 3
# The value of a before swapping is :  2
# The value of b before swapping is :  3
# The value of a after swapping is :  3
# The value of b after swapping is :  2