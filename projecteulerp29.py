LO = 2
HI = 100
termList = []
for a in range(LO, HI + 1):
    for b in range(LO, HI + 1):
        if a**b not in termList:
            termList.append(a**b)
print('ans:', len(termList))
