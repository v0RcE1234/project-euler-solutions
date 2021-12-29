import math
from itertools import permutations

primes = [2]
for i in range(3, 31427):
    for p in primes:
        if i % p == 0:
            break
    else:
        primes.append(i)

def is_prime(n):
    if n < 2:
        return False
    if n in primes:
        return True
    for p in primes:
        if n % p == 0:
            return False
    return True

pandigitalLists = []
for i in range(1, 10):
    pandigitalLists.append(list(range(1, i+1)))
allPandigitals = []
for i in pandigitalLists:
    perms = permutations(i)
    for perm in perms:
        allPandigitals.append(int(''.join([str(j) for j in perm])))

for p in reversed(allPandigitals):
    if is_prime(p):
        ans = p
        break
print(ans)