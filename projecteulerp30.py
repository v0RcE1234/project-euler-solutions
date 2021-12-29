workingNums = []
for i in range(1, 1000000):
    total = 0
    for j in str(i):
        total += int(j)**5
    if total == i:
        workingNums.append(i)
        print(i)

workingNums.remove(1)
print(workingNums)
print('ans:', sum(workingNums))