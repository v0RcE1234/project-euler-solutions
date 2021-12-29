tNums = set()
pNums = set()
hNums = set()
n = 2
while True:
    if n != 285:
        tNums.add(n * (n + 1) / 2)
    pNums.add(n * (3*n - 1) / 2)
    hNums.add(float(n * (2 * n - 1)))
    if len(tNums.intersection(pNums, hNums)) > 0:
        ans = int(list(tNums.intersection(pNums, hNums))[0])
        break
    n += 1
print(ans)