def concatenate_multipliy(n, list):
    out = ''
    for i in list:
        out += str(n*i)
    return int(out)

def isPandigital(n):
    oneToNine = list(range(1, 10))
    for digit in str(n):
        if int(digit) in oneToNine:
            oneToNine.remove(int(digit))
        else:
            return False
    if oneToNine == []:
        return True
    return False

ans = 0

for i in range(10000):
    for j in range(1, 9):
        prod = concatenate_multipliy(i, range(1, j+2))
        if isPandigital(prod) and prod > ans:
            ans = prod
            
print(ans)