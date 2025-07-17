# Calculate the power of a number (x^y)

x = int(input('Enter the base : '))
y = int(input('Enter the power : '))

def power(x,y):
    if y == 0:
        return 1
    else:
        answer = 1
        for i in range(1,y+1):
            answer *= x
        return answer

print(f'{x} to the power {y} is :',power(x,y))

# output
# Enter the base : 2
# Enter the power : 3
# 2 to the power 3 is : 8