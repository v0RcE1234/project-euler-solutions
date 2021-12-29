import math
ansNumer = 1
ansDenom = 1
for d in range(10, 100):
    for n in range(10, d):
        n0 = n // 10
        n1 = n % 10
        d0 = d // 10
        d1 = d % 10
        if (n0 == d1 and n1 * d == d0 * n) or (n1 == d0 and n0 * d == d1 * n):
            ansNumer *= n
            ansDenom *= d
print(ansDenom / math.gcd(ansNumer, ansDenom))
