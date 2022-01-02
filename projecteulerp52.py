from itertools import permutations

x = 1
while True:
    perms = [int(''.join(i)) for i in permutations(str(x))]
    for s in range(2, 7):
        if x * s not in perms:
            break
    else:
        ans = x
        break
    x += 1
print(ans)