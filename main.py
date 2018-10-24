import math

userInput = int(input('Enter the maximum number of the prime series: '))

def checkPrime(numberToCheck):
    if numberToCheck == 2:
        return True
    elif numberToCheck == 3:
        return True
    else:
        limit = int(math.sqrt(numberToCheck)) + 1
        for i in range(2, limit):
            if(numberToCheck % i == 0):
                return False
        return True

for i in range(2, userInput + 1):
    if checkPrime(i):
        print(str(i) + ' ')