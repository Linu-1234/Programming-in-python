# Generate Fibonacci series up to N terms

n = int(input('Enter the term upto which you want the fibonacci series : '))

def fibonacci(n):
    fibonacci_series = [0,1]
    a = 0
    b = 1
    for i in range(2,n):
        sum = a + b
        a = b
        b = sum
        fibonacci_series.append(sum)
    return fibonacci_series

print(f'The fibonacci series upto {n}th term is :',fibonacci(n))


# output
# Enter the term upto which you want the fibonacci series : 5
# The fibonacci series upto 5th term is : [0, 1, 1, 2, 3]
