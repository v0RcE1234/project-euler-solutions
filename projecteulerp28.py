ans = 1
for i in range(3, 1002, 2):
    ans += 4*i**2 - 6*i + 6
print(ans)