import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            break
    else:
        return True
    return False

def allRotations(n):
    allRotations = [n]
    n = list(str(n))
    for i in range(1, len(n)):
        n = [n.copy()[-1], *(n.copy()[:-1])]
        allRotations.append(int(''.join(n)))
    return allRotations

circularPrimes = []
for i in range(1, 1000000):
    for rotation in allRotations(i):
        if not isPrime(rotation):
            break
    else:
        circularPrimes.append(i)
    print(i)
print(circularPrimes, '\n\n\n\n\n\n', len(circularPrimes-1))
