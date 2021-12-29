print("generating primes.")
f = open("abn.out.txt", "w")
primes = [2]
def isprime(n):
    if n <= 1:
        return False
    for i in primes:
        if n%i == 0:
            break
    else:
        primes.append(n)
        return True
    return False
for i in range(3, 107000):
    if isprime(i):
        pass

LO = -999
HI = 1000
print("done generating primes.")
print(primes)
highA = 0   
highB = 0
highN = -1
for a in range(LO, HI):
    for b in range(LO-1, HI+1):
        n = 0
        while ((n**2+a*n+b) in primes):
            n += 1
        if n - 1 > highN:
            highN, highA, highB = n - 1, a, b
        #f.write("%d, %d, %d\n" %(a, b, highN))
    print(a)
print(highA*highB)
f.close()