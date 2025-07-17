# Check if a number is even or odd.

n = int(input('Enter a number : '))

def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
even = iseven(n)

if even == True:
    print(f'{n} is an even number.')
else:
    print(f'{n} is an odd number.')



# output
# Enter a number : 5
# 5 is an odd number.