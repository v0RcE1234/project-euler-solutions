# PROBLEM UNSOLVED - THIS CODE IS INCORRECT

import math
def number_of_digits(n):
    output = 0
    while n > 0:
        output += 1
        n //= 10
    return output

def isprime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            break
    else:
        return True
    return False

circularPrimes = []

for i in range(2, 1000000):
    originalI = i
    if isprime(i):
        allRotations = [i]
        for j in range(1, number_of_digits(i)):     
            X = number_of_digits(i)
            K = ((1 % X) + X) % X
            left_no = i // 10**(X - K)
            i = i % 10**(X - K)
            left_digit = number_of_digits(left_no)
            i = i * 10**left_digit + left_no
        for k in allRotations[1:]:
            if not isprime(k):
                break
        else:
            circularPrimes.append(originalI)
    print(originalI)
print(len(circularPrimes))
