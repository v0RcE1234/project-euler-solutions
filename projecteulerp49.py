from math import sqrt
from itertools import permutations

primes = [2]
def is_prime(n):
    i = max(primes) + 1
    while max(primes) < sqrt(n):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
        i += 1
    for j in primes:
        if n % j == 0:
            return False
    return True

# Generate all four digit primes 
is_prime(100000000)

# Only check above given example
l = 0
for i in primes:
    if i > 1487:
        break
    l += 1

for i in primes[l:]:
    for j in range(1, 3333):
        if i + j in primes and i + 2 * j in primes:
            for k in range(3):
                if not tuple(str(i + k * j)) in permutations(str(i)):
                    break
            else:
                print(i * 100000000 + (i + j) * 10000 + i + 2 * j)
                exit()