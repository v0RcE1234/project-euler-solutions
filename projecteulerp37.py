import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

numTPrimes = 0
sum = 0
currentNumber = 10

while numTPrimes < 11:
    currentNumberEdited = str(currentNumber)
    for i in range(len(currentNumberEdited)):
        if not isPrime(int(currentNumberEdited)):
            break
        currentNumberEdited = currentNumberEdited[:-1]
    else:
        currentNumberEdited = str(currentNumber)
        for i in range(len(currentNumberEdited)):
            if not isPrime(int(currentNumberEdited)):
                break
            currentNumberEdited = currentNumberEdited[1:]
        else:
            numTPrimes += 1
            sum += currentNumber
            print(currentNumber)
    currentNumber += 1

print(sum)