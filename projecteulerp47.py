def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def has_four_p_factors(n):
    return len(prime_factors(n)) == 4

i = 2
while True:
    if has_four_p_factors(i):
        for j in range(i+1, i+4):
            if not has_four_p_factors(j):
                break
        else:
            ans = i
            break
    i += 1
    
print(ans)