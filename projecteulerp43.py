from itertools import permutations

# create list of 0 - 9 pandigitals
allPandigitals = []
l = list(range(10))
perms = permutations(l)
for perm in perms:
    allPandigitals.append(int(''.join([str(j) for j in perm])))

primes = [2, 3, 5, 7, 11, 13, 17]
ans = 0
for p in allPandigitals:
    for firstDigit in range(2, 9):
        if int(str(p)[firstDigit-1:firstDigit+2]) % primes[firstDigit-2] != 0:
           break
    else:
        ans += p
print(ans)