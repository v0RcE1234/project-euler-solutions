import math

primes = [2]
def is_prime(n):
    if n < 2:
        return False
    if n in primes:
        return True
    for p in primes:
        if n % p == 0:
            return False
    primes.append(n)
    return True

perfectSquares = set()
def is_perfect_square(n):
    if n in perfectSquares:
        return True
    if math.sqrt(n).is_integer():
        perfectSquares.add(n)
        return True
    return False

i = 3
while True:
    if i % 2 == 1 and not is_prime(i):
        for j in primes:
            if is_perfect_square(i - j >> 1):
                break
        else:
            ans = i
            break
    i += 1
print(ans)