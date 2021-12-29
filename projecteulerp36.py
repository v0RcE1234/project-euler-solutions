import math
def is_palindrome(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[len(n)-i-1]:
            return False
    return True

sum=0
for i in range(1, 1000000):
    if is_palindrome(i) and is_palindrome(int(bin(i)[2:])):
        sum += i
print(sum)