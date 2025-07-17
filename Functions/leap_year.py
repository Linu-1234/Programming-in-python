# Check if a year is a leap year

n = int(input('Enter the year : '))

def isleapyear(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    else:
        False

leapyear = isleapyear(n)

if leapyear == True:
    print(f'{n} is a leap year.')
else:
    print(f'{n} is not a leap year.')


# output 
# Enter the year : 2020
# 2020 is a leap year.