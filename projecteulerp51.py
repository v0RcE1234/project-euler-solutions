from math import floor, log10, sqrt
from itertools import combinations

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

def num_digits(n):
    return floor(log10(n)) + 1

def any_len_combs(iterable):
    out = []
    for l in range(1, len(iterable)):
        for x in combinations(iterable, l):
            out.append(x)
    return out

def replace_digits(n):
    c = []
    for i in any_len_combs(range(num_digits(n))):
        a = list(str(n))
        b = []
        for j in range(10):
            for k in i:
                a[int(k)] = str(j)
            b.append(int(''.join(a)))
        c.append(b)  
    return c  

i = 2
while True:
    if is_prime(i):
        for j in replace_digits(i):
            primeFamily = []
            for k in j:
                if is_prime(k):
                    primeFamily.append(k)
            if len(primeFamily) == 8:
                print(primeFamily[0])
                exit()        
    i += 1