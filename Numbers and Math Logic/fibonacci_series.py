# Generate the Fibonacci series up to n terms.

n = int(input('Enter the term upto which you want the fibonacci series : '))

a = 0
b = 1

if n <= 0:
    print('Enter a positive number.')
elif n == 1:
    print(a)
else:
    print(f'The fibonacci series upto {n}th term is :')
    print(a)
    print(b)
    for i in range (1,n-1):
        sum = a + b
        print(sum)
        a = b
        b = sum

# output
# Enter the term upto which you want the fibonacci series : 5
# The fibonacci series upto 5th term is :
# 0
# 1
# 1
# 2
# 3
