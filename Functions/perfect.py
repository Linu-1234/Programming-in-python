# Check if a number is Perfect

n = int(input('Enter a number : '))

def isperfect(n):
    num = n
    divisors =[]
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            divisors.append(i)
            sum += i
    return num == sum

perfect = isperfect(n)

if perfect == True:
    print(f'{n} is a perfect number.')
else:
    print(f'{n} is not a perfect number.')


# output
# Enter a number : 28
# 28 is a perfect number.
    

