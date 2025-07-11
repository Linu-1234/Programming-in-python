# Check if a Number is Prime or not.

n = int(input('Enter a number : '))

isprime = True

if n <= 1:
    isprime = False

else:
    # for i in range (2,n): #For Time Complexity O(n)
    for i in range (2,int(n**0.5)+1): #For Time Complexity O(√n)
        if n % i == 0:
            isprime = False
            break

if isprime == False:
    print(f'{n} is not a prime number.')
else:
    print(f'{n} is a prime number.')


# output 
# Enter a number : 5
# 5 is a prime number.