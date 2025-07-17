# Check if a number is prime

n = int(input('Enter a number : '))

def isprime(n):
    if n <= 1:
        return False
    else:
        prime = True
        for i in range(2,n):
            if n % i == 0:
                prime = False
                break
        if prime == True:
            return True
        else:
            return False
    
prime = isprime(n)
if prime == True:
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not a prime number.')



# output
# Enter a number : 2
# 2 is a prime number.