import math
workingNums = []
for i in range(3, 2540161):
    total = 0
    for j in str(i):
        total += math.factorial(int(j))
    if i == total:
        workingNums.append(i)
    print(i)

print(workingNums)
print(sum(workingNums))