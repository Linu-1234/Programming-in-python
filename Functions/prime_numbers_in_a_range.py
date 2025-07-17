# Print all prime numbers in a given range

a = int(input('Enter the min range : '))
b = int(input('Enter the max range : '))

def prime(a,b):
    prime_numbers = []
    for i in range(a,b+1):
        if i < 2:
            continue
        isprime = True
        for j in range(2,i):
            if i % j == 0:
                isprime = False
                break
        if isprime == True:
            prime_numbers.append(i)
    return prime_numbers


print(f'The prime numbers in the range {a} and {b} is :',prime(a,b))


# output
# Enter the min range : 1
# Enter the max range : 20
# The prime numbers in the range 1 and 20 is : [2, 3, 5, 7, 11, 13, 17, 19]