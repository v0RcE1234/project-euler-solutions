from math import factorial

def choose(n, r):
    return factorial(n)/(factorial(r)*factorial(n - r))

ans = 0
for n in range(101):
    for r in range(n):
        if choose(n, r) > 1000000:
            ans += 1
print(ans)